package com.example.stevtourguidev5;

import android.graphics.Color;
import android.support.constraint.ConstraintLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

public class tgmLecHall extends AppCompatActivity {

    public int state = 0;
    public ConstraintLayout c1;
    public ImageView nextStep, backStep;
    public ImageView lecHall2;
    public TextView msg1, msg2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tgm_lec_hall);
        c1 = (ConstraintLayout) findViewById(R.id.ConstraintLayout1);

        nextStep = (ImageView) findViewById(R.id.nextButton2);
        backStep = (ImageView) findViewById(R.id.backButton2);

        msg1 = (TextView) findViewById(R.id.lecHallStartMsg);
        msg2 = (TextView) findViewById(R.id.lecHallMsg2);

        lecHall2 = (ImageView) findViewById(R.id.tgmLecHall2);



        nextStep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (state == 0) {
                    c1.setBackgroundResource(R.drawable.tgmlechall2);
                    msg2.setVisibility(View.VISIBLE);
                    msg1.setVisibility(View.INVISIBLE);
                    state = 1;
                } else if (state == 1) {

                } else if (state == 2) {

                }
            }
        });

        backStep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (state == 1) {
                    c1.setBackgroundResource(R.drawable.tgmlechall1);
                    msg2.setVisibility(View.VISIBLE);
                    msg2.setVisibility(View.INVISIBLE);
                    state = 0;
                } else if (state == 2) {

                } else if (state == 3) {

                }
            }
        });

    }
}
