package com.example.stevtourguidev5;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class menu extends AppCompatActivity {

    public TextView greet1, greet2, greet3, greet4;
    public ImageView nextImg, backImg;
    public Button findARoomButton, tourGuideModeButton;
    public int state = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        nextImg = (ImageView) findViewById(R.id.nextButton);
        backImg = (ImageView) findViewById(R.id.backButton);

        greet1 = (TextView) findViewById(R.id.greeting1);
        greet2 = (TextView) findViewById(R.id.greeting2);
        greet3 = (TextView) findViewById(R.id.greeting3);
        greet4 = (TextView) findViewById(R.id.greeting4);

        findARoomButton = (Button) findViewById(R.id.farButton);
        tourGuideModeButton = (Button) findViewById(R.id.tgmButton);

        nextImg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (state == 0) {
                    greet2.setVisibility(View.VISIBLE);
                    greet1.setVisibility(View.INVISIBLE);
                    state = 1;
                } else if (state == 1) {
                    greet3.setVisibility(View.VISIBLE);
                    greet2.setVisibility(View.INVISIBLE);
                    state = 2;
                } else if (state == 2) {
                    greet4.setVisibility(View.VISIBLE);
                    greet3.setVisibility(View.INVISIBLE);
                    state = 3;
                    findARoomButton.setVisibility(View.VISIBLE);
                    tourGuideModeButton.setVisibility(View.VISIBLE);
                }
            }
        });

        backImg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (state == 1) {
                  greet1.setVisibility(View.VISIBLE);
                  greet2.setVisibility(View.INVISIBLE);
                  state = 0;
                } else if (state == 2) {
                  greet2.setVisibility(View.VISIBLE);
                  greet3.setVisibility(View.INVISIBLE);
                  state = 1;
                } else if (state == 3) {
                  greet3.setVisibility(View.VISIBLE);
                  greet4.setVisibility(View.INVISIBLE);
                  findARoomButton.setVisibility(View.GONE);
                  tourGuideModeButton.setVisibility(View.GONE);
                  state = 2;
                }
            }
        });

        tourGuideModeButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                openTgmMenu(v);
            }
        });

        findARoomButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //openFarMenu(v);
            }
        });
    }

    public void openTgmMenu(View view) {
        Intent intent = new Intent(menu.this, tgmMenu.class);
        startActivity(intent);
    }

}
