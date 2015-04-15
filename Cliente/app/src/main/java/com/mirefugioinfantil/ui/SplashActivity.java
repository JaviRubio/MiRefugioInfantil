package com.mirefugioinfantil.ui;


import android.app.Activity;
import android.content.Intent;
import android.graphics.PixelFormat;
import android.os.Bundle;
import android.os.Handler;
import android.view.Window;
import android.view.WindowManager;

import com.mirefugioinfantil.R;

/**
 * Clase inicial puramente estetica. Muestra un splash durante 2 segundos
 * @author Namir Sayed-Ahmad Baraza
 * @mail namirsab@gmail.com
 *
 */
public class SplashActivity extends Activity {
	//Tiempo de splash en milisegundos
	protected int splashTime = 2000;
    protected Class nextActivity = MainActivity.class;
    protected int splashView = R.layout.splash;
	@Override
	protected void onStart() {
		// TODO Auto-generated method stub
		super.onStart();
	}
	
	@Override
	protected void onStop() {
		// TODO Auto-generated method stub
		super.onStop();
	}

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		// TODO Auto-generated method stub
		super.onCreate(savedInstanceState);

        this.getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
		this.requestWindowFeature(Window.FEATURE_NO_TITLE);
		getWindow().setFormat(PixelFormat.RGBA_8888);
		setContentView(this.splashView);
		getApplicationContext();
        final Intent intent = new Intent(SplashActivity.this, this.nextActivity);
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
