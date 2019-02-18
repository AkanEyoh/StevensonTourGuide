package com.example.akaneyoh.stevtourguidev3;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.os.Handler;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class Main3Activity extends AppCompatActivity {

    private TextView fullPrintStatement;
    private String printedPath = "";
    private RequestQueue mQueue;
    private String errorMessage = "Sorry, one of those rooms does not exist. " +
            "Please enter a valid room number.";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        fullPrintStatement = findViewById(R.id.printStatement);
        Button showPathButton = findViewById(R.id.pathButton);

        mQueue = Volley.newRequestQueue(this);

        showPathButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                jsonParse();
            }
        });
    }

    private void jsonParse() {
        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, Main2Activity.urlPath, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            JSONArray jsonArray = response.getJSONArray("return_list");
                            if (jsonArray.getString(0).equals("False")) {
                                printedPath = "Sorry, either one or both of those rooms do not exist within Stevenson. " +
                                        "Please enter valid room numbers and try again.";
                                fullPrintStatement.append(printedPath);
                                new Handler().postDelayed(new Runnable() {
                                    @Override
                                    public void run() {
                                        Intent i = new Intent(Main3Activity.this, Main2Activity.class);
                                        startActivity(i);
                                        finish();
                                    }
                                }, 5000);
                            } else {
                                for (int i = 0; i < jsonArray.length(); i++) {
                                    if (jsonArray.getString(i) != "null") {
                                        printedPath = printedPath + "\n" + jsonArray.getString(i));
                                    }
                                }
                                String intro = "You are currently located at Room " + Main2Activity.startRoom + ". "
                                        + "Use the following instructions to reach Room " + Main2Activity.endRoom + ".\n";
                                fullPrintStatement.append(intro);
                                fullPrintStatement.append(printedPath);
                                String closing = "\n\nCongratulations, you made it to Room " + Main2Activity.endRoom + "!"
                                        + "\nThank you for using Stevenson Tour Guide. :)";
                                fullPrintStatement.append(closing);
                            }
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                error.printStackTrace();
            }
        });
        mQueue.add(request);
    }
}
