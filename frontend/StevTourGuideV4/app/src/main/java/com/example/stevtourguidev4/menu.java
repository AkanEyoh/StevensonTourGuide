package com.example.stevtourguidev4;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.Timer;
import java.util.TimerTask;

public class menu extends AppCompatActivity {

    public Button button2;
    public Button tgmButton;
    public Button farButton;
    public TextView greet1;
    public TextView greet2;
    public TextView greet3;
    Timer timer;
    Timer timer2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
        tgmButton = (Button) findViewById(R.id.tourGuideModeButton);
        tgmButton.setVisibility(View.INVISIBLE);
        farButton = (Button) findViewById(R.id.findARoomButton);
        farButton.setVisibility(View.INVISIBLE);

        greet1 = (TextView) findViewById(R.id.intro1);
        greet2 = (TextView) findViewById(R.id.intro2);
        greet2.setVisibility(View.INVISIBLE);
        greet3 = (TextView) findViewById(R.id.intro3);
        greet3.setVisibility(View.INVISIBLE);

        timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                greet1.setVisibility(View.INVISIBLE);
                greet2.setVisibility(View.VISIBLE);
            }
        }, 4000);

        timer2 = new Timer();
        timer2.schedule(new TimerTask() {
            @Override
            public void run() {
                greet2.setVisibility(View.INVISIBLE);
                greet3.setVisibility(View.VISIBLE);
                tgmButton.setVisibility(View.VISIBLE);
                farButton.setVisibility(View.VISIBLE);
            }
        }, 3000);

        button2 = (Button) findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tgmSelect(v);
            }
        });

        tgmButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                tgmSelect(v);
            }
        });
    }

    public void tgmSelect(View view) {
        Intent intent = new Intent(menu.this, tgm_menu.class);
        startActivity(intent);
    }
}
