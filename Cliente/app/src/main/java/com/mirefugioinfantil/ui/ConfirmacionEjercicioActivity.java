package com.mirefugioinfantil.ui;

import android.app.Activity;
import android.content.Intent;
import android.graphics.PixelFormat;
import android.os.Bundle;
import android.os.Handler;
import android.view.Window;
import android.view.WindowManager;

import com.mirefugioinfantil.R;

public class ConfirmacionEjercicioActivity extends Activity {

    protected int splashTime = 2500;
    protected Class nextActivity = BuscarEjercicioActivity.class;
    protected int splashView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        splashView = this.getIntent().getIntExtra(RealizarEjercicioNFCActivity.SPLASH, R.layout.activity_confirmacion_ejercicio);
        this.requestWindowFeature(Window.FEATURE_NO_TITLE);
        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        getWindow().setFormat(PixelFormat.RGBA_8888);
        setContentView(this.splashView);
        getApplicationContext();
        final Intent intent = new Intent(this, this.nextActivity);
        intent.setFlags(Intent.FLAG_ACTIVITY_REORDER_TO_FRONT);
        new Handler().postDelayed(new Runnable(){
            public void run(){
					/*Pasados los dos segundos inicia la activity "activityApp"*/
                startActivity(intent);
					/*Destruye esta*/
                finish();
            };

        }, this.splashTime);

    }



}
