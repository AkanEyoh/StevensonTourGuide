package com.example.stevtourguidev5;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class farmMenu extends AppCompatActivity {

    public static final String urlBase = "10.66.140.12";
    private static final String directionsPort = "8000";
    public static String urlPath;
    public static String startRoom;
    public static String endRoom;

    EditText startRoomInput;
    EditText endRoomInput;

    Button findRoomButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_farm_menu);

        startRoomInput = findViewById(R.id.startRoomInput);
        endRoomInput = findViewById(R.id.endRoomInput);

        findRoomButton = findViewById(R.id.find_a_room_button);
        findRoomButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startRoom = startRoomInput.getText().toString();
                endRoom = endRoomInput.getText().toString();

                urlPath = "http://" + urlBase + ":" + directionsPort + "/routeFinder/" + startRoom + "/" + endRoom;
                openActivity3(v);
            }
        });
    }
// add picasso gradle build file
    public void openActivity3(View view) {
        Intent intent = new Intent(farmMenu.this, Main3Activity.class);
        startActivity(intent);
    }
}
