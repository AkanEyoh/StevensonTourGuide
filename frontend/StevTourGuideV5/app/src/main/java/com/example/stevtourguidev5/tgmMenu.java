package com.example.stevtourguidev5;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class tgmMenu extends AppCompatActivity {

    public Button lecHall;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tgm_menu);

        lecHall = (Button) findViewById(R.id.lecHallButton);

        lecHall.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openLecHallTGM(v);
            }
        });
    }

    public void openLecHallTGM(View view) {
        Intent intent = new Intent(tgmMenu.this, tgmLecHall.class);
        startActivity(intent);
    }
}
