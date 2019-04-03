package com.example.akaneyoh.stevtourguidev3;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
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

import com.squareup.picasso.*;

public class Main3Activity extends AppCompatActivity {
    private final int[] textIds = {R.id.t1, R.id.t2, R.id.t3, R.id.t4};
    private final int[] imageIds = {R.id.i1, R.id.i2, R.id.i3, R.id.i4};
    private final String imageServerUrlBase = "http://10.66.79.151:7777/";

    private RequestQueue mQueue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        mQueue = Volley.newRequestQueue(this);

        jsonParse();
    }

    private void jsonParse() {
        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, Main2Activity.urlPath, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            String[] directions = jsonArrToArray(response.getJSONArray("directions"));
                            String[] urls = jsonArrToArray(response.getJSONArray("urls"));
                            if (directions == null) {
                                // TODO add error msg if this fails

                                // TODO re-add below
                                /*new Handler().postDelayed(new Runnable() {
                                    @Override
                                    public void run() {
                                        Intent i = new Intent(Main3Activity.this, Main2Activity.class);
                                        startActivity(i);
                                        finish();
                                    }
                                }, 5000);*/
                            } else {
                                loadDirections(directions, urls);
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

    private String[] jsonArrToArray(JSONArray arr) {
        if (arr == null || arr.length() == 0)
            return null;

        String[] converted = new String[arr.length()];

        for (int i=0; i < converted.length; i++) {
            try {
                converted[i] = arr.getString(i);
            } catch (JSONException e) {
                // this really shouldn't happen...
                return null;
            }
        }
        return converted;
    }

    public void loadDirections(String[] directionText, String[] imageUrls) {
        int numDirections = directionText.length;
        for (int i=0; i < numDirections; i++) {
            addDirection(textIds[i], imageIds[i], directionText[i], imageUrls[i]);
        }
    }

    public void addDirection(int textId, int imageId, String text, String url) {
        // first change the text item
        TextView targetText = (TextView) findViewById(textId);
        targetText.setText(text);
        targetText.setVisibility(View.VISIBLE);

        // now change the image
        ImageView targetImage = (ImageView) findViewById(imageId);
        Picasso
                .get()
                .load(imageServerUrlBase + url)
                .error(R.drawable.camel)
                .resize(1000, 1000)
                .rotate(90)
                .into(targetImage);
        targetImage.setVisibility(View.VISIBLE);
    }
}
