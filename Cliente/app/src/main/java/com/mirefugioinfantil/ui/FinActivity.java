package com.mirefugioinfantil.ui;

import com.mirefugioinfantil.R;
import com.mirefugioinfantil.modelo.Actividad;
import com.mirefugioinfantil.modelo.Ejercicio;
import com.mirefugioinfantil.modelo.IdentificadorNFC;
import com.mirefugioinfantil.modelo.Resultado;
import com.mirefugioinfantil.net.RefugioAPIClient;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import com.j256.ormlite.dao.Dao;
import com.j256.ormlite.table.TableUtils;
import com.loopj.android.http.AsyncHttpResponseHandler;


import android.os.Bundle;
import android.widget.TextView;


import org.apache.http.Header;

import java.sql.SQLException;
import java.util.List;


public class FinActivity extends DBHandlerNFCActivity {

    private TextView tView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        tView = (TextView) findViewById(R.id.fullscreen_content);
        tView.setText("CONFIRMA");

    }

    @Override
    public void onNFCReceived(String datosNFC) {
        if(datosNFC.equalsIgnoreCase(IdentificadorNFC.FIN)){
            enviarResultados();
            tView.setText("HASTA LUEGO");
            finish();


        }
    }

    private void enviarResultados() {
        //Obtener de la base de datos todos los resultados de la sesión
        try {
            Dao resDao = getHelper().getResultadoDao();
            List<Resultado> resultados = resDao.queryForAll();

            if (resultados.size() > 0) {
                //List<Actividad> actividades = gson.fromJson(response.toString(), new TypeToken<List<Actividad>>(){}.getType());
                Gson gson = new GsonBuilder().excludeFieldsWithoutExposeAnnotation().create(); // .setDateFormat() <- Tener en cuenta
                String json = gson.toJson(resultados, new TypeToken<List<Resultado>>() {
                }.getType());
                //Enviarlos al servidor
                RefugioAPIClient.post("api/resultados", null, json, new AsyncHttpResponseHandler() {
                    @Override
                    public void onSuccess(int statusCode, Header[] headers, byte[] response) {
                        //super.onSuccess(statusCode, headers, response);
                        //DROP TABLE RESULTADO
                        try {
                            TableUtils.clearTable(getHelper().getConnectionSource(), Resultado.class);
                        } catch (SQLException e) {
                            e.printStackTrace();
                        }
                    }

                    @Override
                    public void onFailure(int i, Header[] headers, byte[] bytes, Throwable throwable) {

                    }

                });

            }
            TableUtils.clearTable(getHelper().getConnectionSource(), Ejercicio.class);
            TableUtils.clearTable(getHelper().getConnectionSource(), Actividad.class);
            logout();
        }catch(SQLException e){
            logout();
        }

    }

    private void logout(){
        RefugioAPIClient.get("api/logout", null, new AsyncHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers, byte[] response) {
            }

            @Override
            public void onFailure(int i, Header[] headers, byte[] bytes, Throwable throwable) {
            }
        });
    }
}
