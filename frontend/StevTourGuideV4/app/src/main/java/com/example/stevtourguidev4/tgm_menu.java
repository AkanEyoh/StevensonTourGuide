package com.example.stevtourguidev4;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

public class tgm_menu extends AppCompatActivity {

    public Button lecHallButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tgm_menu);

        lecHallButton = (Button) findViewById(R.id.lectureHallButton);
        lecHallButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openLecHallTGM(v);
            }
        });
    }
    public void openLecHallTGM(View view) {
        Intent intent = new Intent(tgm_menu.this, lecHallTourGuideMode.class);
        startActivity(intent);
    }
}
