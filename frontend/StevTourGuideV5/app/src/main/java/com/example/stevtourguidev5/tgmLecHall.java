package com.example.stevtourguidev5;

import android.content.Intent;
import android.support.constraint.ConstraintLayout;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import org.w3c.dom.Text;

public class tgmLecHall extends AppCompatActivity {

    public int state = 0;
    public ConstraintLayout c1;
    public ImageView nextStep, backStep;
    public TextView msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9, msg10, msg11, msg12;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_tgm_lec_hall);
        c1 = (ConstraintLayout) findViewById(R.id.ConstraintLayout1);

        nextStep = (ImageView) findViewById(R.id.nextButton2);
        backStep = (ImageView) findViewById(R.id.backButton2);

        msg1 = (TextView) findViewById(R.id.lecHallStartMsg);
        msg2 = (TextView) findViewById(R.id.lecHallMsg2);
        msg3 = (TextView) findViewById(R.id.lecHallMsg3);
        msg4 = (TextView) findViewById(R.id.lecHallMsg4);
        msg5 = (TextView) findViewById(R.id.lecHallMsg5);
        msg6 = (TextView) findViewById(R.id.lecHallMsg6);
        msg7 = (TextView) findViewById(R.id.lecHallMsg7);
        msg8 = (TextView) findViewById(R.id.lecHallMsg8);
        msg9 = (TextView) findViewById(R.id.lecHallMsg9);
        msg10 = (TextView) findViewById(R.id.lecHallMsg10);
        msg11 = (TextView) findViewById(R.id.lecHallMsg11);
        msg12 = (TextView) findViewById(R.id.lecHallMsg12);

        nextStep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (state == 0) {
                    c1.setBackgroundResource(R.drawable.tgmlechall2);
                    msg2.setVisibility(View.VISIBLE);
                    msg1.setVisibility(View.INVISIBLE);
                    state = 1;
                } else if (state == 1) {
                    c1.setBackgroundResource(R.drawable.tgmlechall3);
                    msg3.setVisibility(View.VISIBLE);
                    msg2.setVisibility(View.INVISIBLE);
                    state = 2;
                } else if (state == 2) {
                    c1.setBackgroundResource(R.drawable.tgmlechall4);
                    msg4.setVisibility(View.VISIBLE);
                    msg3.setVisibility(View.INVISIBLE);
                    state = 3;
                } else if (state == 3) {
                    msg5.setVisibility(View.VISIBLE);
                    msg4.setVisibility(View.INVISIBLE);
                    state = 4;
                } else if (state == 4) {
                    c1.setBackgroundResource(R.drawable.tgmlechall5);
                    msg6.setVisibility(View.VISIBLE);
                    msg5.setVisibility(View.INVISIBLE);
                    state = 5;
                } else if (state == 5) {
                    c1.setBackgroundResource(R.drawable.tgmlechall6);
                    msg7.setVisibility(View.VISIBLE);
                    msg6.setVisibility(View.INVISIBLE);
                    state = 6;
                } else if (state == 6) {
                    msg8.setVisibility(View.VISIBLE);
                    msg7.setVisibility(View.INVISIBLE);
                    state = 7;
                } else if (state == 7) {
                    c1.setBackgroundResource(R.drawable.tgmlechall7);
                    msg9.setVisibility(View.VISIBLE);
                    msg8.setVisibility(View.INVISIBLE);
                    state = 8;
                } else if (state == 8) {
                    c1.setBackgroundResource(R.drawable.tgmlechall8);
                    msg10.setVisibility(View.VISIBLE);
                    msg9.setVisibility(View.INVISIBLE);
                    state = 9;
                } else if (state == 9) {
                    c1.setBackgroundResource(R.drawable.tgmlechall9);
                    msg11.setVisibility(View.VISIBLE);
                    msg10.setVisibility(View.INVISIBLE);
                    state = 10;
                } else if (state == 10) {
                    c1.setBackgroundResource(R.drawable.tgmlechall10);
                    msg12.setVisibility(View.VISIBLE);
                    msg11.setVisibility(View.INVISIBLE);
                    state = 11;
                }
            }
        });

        backStep.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (state == 0) {
                    openTgmMenu(v);
                } else if (state == 1) {
                    c1.setBackgroundResource(R.drawable.tgmlechall1);
                    msg1.setVisibility(View.VISIBLE);
                    msg2.setVisibility(View.INVISIBLE);
                    state = 0;
                } else if (state == 2) {
                    c1.setBackgroundResource(R.drawable.tgmlechall2);
                    msg2.setVisibility(View.VISIBLE);
                    msg3.setVisibility(View.INVISIBLE);
                    state = 1;
                } else if (state == 3) {
                    c1.setBackgroundResource(R.drawable.tgmlechall3);
                    msg3.setVisibility(View.VISIBLE);
                    msg4.setVisibility(View.INVISIBLE);
                    state = 2;
                } else if (state == 4) {
                    msg4.setVisibility(View.VISIBLE);
                    msg5.setVisibility(View.INVISIBLE);
                    state = 3;
                } else if (state == 5) {
                    c1.setBackgroundResource(R.drawable.tgmlechall4);
                    msg5.setVisibility(View.VISIBLE);
                    msg6.setVisibility(View.INVISIBLE);
                    state = 4;
                } else if (state == 6) {
                    c1.setBackgroundResource(R.drawable.tgmlechall5);
                    msg6.setVisibility(View.VISIBLE);
                    msg7.setVisibility(View.INVISIBLE);
                    state = 5;
                } else if (state == 7) {
                    msg7.setVisibility(View.VISIBLE);
                    msg8.setVisibility(View.INVISIBLE);
                    state = 6;
                } else if (state == 8) {
                    c1.setBackgroundResource(R.drawable.tgmlechall6);
                    msg8.setVisibility(View.VISIBLE);
                    msg9.setVisibility(View.INVISIBLE);
                    state = 7;
                } else if (state == 9) {
                    c1.setBackgroundResource(R.drawable.tgmlechall7);
                    msg9.setVisibility(View.VISIBLE);
                    msg10.setVisibility(View.INVISIBLE);
                    state = 8;
                } else if (state == 10) {
                    c1.setBackgroundResource(R.drawable.tgmlechall8);
                    msg10.setVisibility(View.VISIBLE);
                    msg11.setVisibility(View.INVISIBLE);
                    state = 9;
                } else if (state == 11) {
                    c1.setBackgroundResource(R.drawable.tgmlechall9);
                    msg11.setVisibility(View.VISIBLE);
                    msg12.setVisibility(View.INVISIBLE);
                    state = 10;
                }
            }
        });

    }

    public void openTgmMenu(View view) {
        Intent intent = new Intent(tgmLecHall.this, tgmMenu.class);
        startActivity(intent);
    }
}
