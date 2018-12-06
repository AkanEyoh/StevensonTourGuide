package com.example.akaneyoh.stevtourguidev3;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Main2Activity extends AppCompatActivity {

    public static String urlPath;
    public static String startRoom;
    public static String endRoom;

    EditText startRoomInput;
    EditText endRoomInput;

    Button findRoomButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        startRoomInput = findViewById(R.id.startRoomInput);
        endRoomInput = findViewById(R.id.endRoomInput);

        findRoomButton = findViewById(R.id.findRoomButton);
        findRoomButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startRoom = startRoomInput.getText().toString();
                endRoom = endRoomInput.getText().toString();

                urlPath = "http://10.66.45.42:5000/routeFinder/" + startRoom + "/" + endRoom;
                openActivity3(v);
            }
        });
    }

    public void openActivity3(View view) {
        Intent intent = new Intent(Main2Activity.this, Main3Activity.class);
        startActivity(intent);
    }
}
