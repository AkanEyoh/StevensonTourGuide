package com.example.akaneyoh.stevtourguidev3;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

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

    private TextView printedPath;
    private RequestQueue mQueue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        printedPath = findViewById(R.id.pathArray);
        Button showPathButton = findViewById(R.id.pathButton);

        mQueue = Volley.newRequestQueue(this);

        showPathButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String intro = "You are currently located at Room " + Main2Activity.startRoom + ". "
                        + "Use the following instructions to reach Room " + Main2Activity.endRoom + ".\n\n";
                String closing = "\n\nCongratulations, you made it to Room " + Main2Activity.endRoom + "!"
                        + "\nThank you for using Stevenson Tour Guide. :)";
                printedPath.append(intro);
                jsonParse();
                printedPath.append(closing);
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
                            for (int i = 0; i < jsonArray.length(); i++) {
                                JSONObject locationCode = jsonArray.getJSONObject(i);
                                String location = locationCode.toString();
                                printedPath.append(location);
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
