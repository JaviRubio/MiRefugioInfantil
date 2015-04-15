package com.mirefugioinfantil.ui;

import android.content.Intent;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.widget.TextView;

import com.mirefugioinfantil.R;
import com.mirefugioinfantil.modelo.Ejercicio;
import com.mirefugioinfantil.modelo.IdentificadorNFC;
import com.mirefugioinfantil.modelo.Resultado;
import com.j256.ormlite.dao.Dao;

import java.sql.SQLException;

public class RealizarEjercicioNFCActivity extends DBHandlerNFCActivity {

    private Ejercicio activo;
    private static long TIEMPO_ACTIVO = 30000;
    private Resultado resultadoActivo;
    private Integer numeroAciertos = 0;
    private long tiempoTranscurrido;
    public final static String SPLASH = "com.mirefugioinfantil.splash";
    private CountDownTimer temporizador;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        activo = this.getIntent().getParcelableExtra(BuscarEjercicioActivity.EJERCICIO);
        TextView textView = (TextView) findViewById(R.id.fullscreen_content);
        textView.setText(activo.getPregunta());
        resultadoActivo = new Resultado();
        tiempoTranscurrido = System.currentTimeMillis();
        //TIEMPO_ACTIVO+1 para que nunca ejecute la funcion onTick()
        temporizador = new CountDownTimer(TIEMPO_ACTIVO*activo.cuantasSoluciones(),TIEMPO_ACTIVO*activo.cuantasSoluciones()+1){

            @Override
            public void onTick(long l) {
            }

            @Override
            public void onFinish() {
                guardarSolucion();
                cargarSplash(R.layout.activity_timeup_ejercicio);
            }


        }.start();
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


    @Override
    public void onNFCReceived(String datosNFC) {
        //Evaluar el NFC leido
        String[] datosNFCsplit = datosNFC.split(IdentificadorNFC.SEPARADOR);
        if(datosNFCsplit[0].equalsIgnoreCase(IdentificadorNFC.ITEM_ACTIVIDAD)){

            String[] NFCActividad;
            boolean esRespuestaCorrecta = false, incluida = false;

            for(int i=1; i < datosNFCsplit.length ;i++) {
                NFCActividad = datosNFCsplit[i].split(IdentificadorNFC.SEPARADOR_ITEM);
                String idActividad = String.valueOf(this.getIntent().getIntExtra(BuscarEjercicioActivity.ID_ACTIVIDAD, -1));
                if(NFCActividad[0].equalsIgnoreCase(idActividad)){
                    incluida = resultadoActivo.estaIncluida(NFCActividad[1]);
                    resultadoActivo.actualizarResultado(NFCActividad[1]);
                    esRespuestaCorrecta = activo.esCorrecta(NFCActividad[1]);
                    break;
                }
            }

            if(esRespuestaCorrecta && !incluida){
                numeroAciertos++;
                if(numeroAciertos.equals(activo.cuantasSoluciones())) {
                    resultadoActivo.setTiempo_respuesta(System.currentTimeMillis() - tiempoTranscurrido);
                    temporizador.cancel();
                    guardarSolucion();
                    cargarSplash(R.layout.activity_confirmacion_ejercicio);
                }
            }
        }
    }
}
