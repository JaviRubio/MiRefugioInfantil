package com.mirefugioinfantil.ui;

import com.mirefugioinfantil.R;
import com.mirefugioinfantil.database.DBHelper;
import com.mirefugioinfantil.modelo.Ejercicio;
import com.mirefugioinfantil.modelo.Resultado;
import com.j256.ormlite.android.apptools.OpenHelperManager;
import com.j256.ormlite.dao.Dao;

import android.app.Activity;
import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.view.Window;
import android.view.WindowManager;
import android.widget.TextView;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;


public class RealizarEjercicioAcelerometro extends BaseActivity implements SensorEventListener {

    private static long TIEMPO_ACTIVO = 15000;
    private static float TASA_MOVIMIENTO = 0.75f;
    private static int SUAVE = 0;
    private static int BRUSCO = 1;
    public final static String SPLASH = "com.mirefugioinfantil.splash";

    private DBHelper dbHelper;
    private Ejercicio activo;
    private Resultado resultadoActivo;
    private List<Integer> resultadoEnProceso;

    float lastX = 0;
    float lastY = 0;
    float lastZ = 0;
    long lastUpdate = System.currentTimeMillis();

    public DBHelper getHelper() {
        if (dbHelper == null) {
            dbHelper = OpenHelperManager.getHelper(this, DBHelper.class);
        }
        return dbHelper;
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (dbHelper != null) {
            OpenHelperManager.releaseHelper();
            dbHelper = null;
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        activo = this.getIntent().getParcelableExtra(BuscarEjercicioActivity.EJERCICIO);

        TextView tView = (TextView) findViewById(R.id.fullscreen_content);
        tView.setText(activo.getPregunta());

        resultadoActivo = new Resultado();
        resultadoEnProceso = new ArrayList<Integer>();
        new CountDownTimer(TIEMPO_ACTIVO*activo.cuantasSoluciones(),TIEMPO_ACTIVO+1){

            @Override
            public void onTick(long l) {
            }

            @Override
            public void onFinish() {
                int respuesta = construirSolucion();
                resultadoActivo.actualizarResultado(String.valueOf(respuesta));
                guardarSolucion();
                if(activo.getSolucion().equalsIgnoreCase(String.valueOf(respuesta)))
                    cargarSplash(R.layout.activity_confirmacion_ejercicio);
                else
                    cargarSplash(R.layout.activity_timeup_ejercicio);

            }
        }.start();
    }




    @Override
    protected void onResume() {
        super.onResume();
        this.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT);
        SensorManager sm = (SensorManager) getSystemService(SENSOR_SERVICE);
        List<Sensor> sensors = sm.getSensorList(Sensor.TYPE_LINEAR_ACCELERATION);
        sm.registerListener(this, sensors.get(0), SensorManager.SENSOR_DELAY_GAME);
    }




    @Override
    public void onSensorChanged(SensorEvent sensorEvent) {
        long curTime = System.currentTimeMillis();
        float curX = sensorEvent.values[0];
        float curY = sensorEvent.values[1];
        float curZ = sensorEvent.values[2];

        if ((curTime - lastUpdate) > 1000 ) {
            if(Math.abs(curX - lastX) > 6 || Math.abs(curY - lastY) > 6 || Math.abs(curZ - lastZ) > 6) {
                añadirMovimiento(BRUSCO);
            }
            else if ( 6 > Math.abs(curX - lastX) && Math.abs(curX - lastX) > 0.7
                    && 6 > Math.abs(curY - lastY) && Math.abs(curY - lastY) > 0.7
                    && 6 > Math.abs(curZ - lastZ) && Math.abs(curZ - lastZ) > 0.7) {
                añadirMovimiento(SUAVE);
            }
            lastX = curX;
            lastY= curY;
            lastZ = curZ;
            lastUpdate = curTime;
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int i) {

    }

    private void añadirMovimiento(int movimiento){

        resultadoEnProceso.add(movimiento);
    }

    private int construirSolucion(){
        int contador = 0;
        for(int i=0; i < resultadoEnProceso.size(); i++){
            if(resultadoEnProceso.get(i) == BRUSCO) contador++;
        }

        if(contador > (resultadoEnProceso.size() * TASA_MOVIMIENTO) ) return BRUSCO;
        else return SUAVE;

    }

    private void cargarSplash(int idSplash){
        Intent intent = new Intent(this, ConfirmacionEjercicioActivity.class);
        intent.putExtra(SPLASH, idSplash);
        startActivity(intent);
        finish();
    }

    private void guardarSolucion() {
        resultadoActivo.setEjercicio(activo.getId());
        resultadoActivo.setActividad(this.getIntent().getIntExtra(BuscarEjercicioActivity.ID_ACTIVIDAD, -1));
        try {
            Dao resDao = getHelper().getResultadoDao();
            resDao.createIfNotExists(resultadoActivo);
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }

}
