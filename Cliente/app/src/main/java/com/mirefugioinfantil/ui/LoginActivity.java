package com.mirefugioinfantil.ui;

import com.mirefugioinfantil.R;
import com.mirefugioinfantil.modelo.Actividad;
import com.mirefugioinfantil.modelo.Ejercicio;
import com.mirefugioinfantil.net.RefugioAPIClient;
import com.mirefugioinfantil.ui.util.SystemUiHider;

import android.annotation.TargetApi;
import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import com.j256.ormlite.dao.Dao;
import com.loopj.android.http.JsonHttpResponseHandler;

import org.apache.http.Header;
import org.json.JSONArray;

import java.sql.SQLException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 *
 * @see SystemUiHider
 */
public class LoginActivity extends DBHandlerNFCActivity {



    /**
     * Whether or not the system UI should be auto-hidden after
     * {@link #AUTO_HIDE_DELAY_MILLIS} milliseconds.
     */
    private static final boolean AUTO_HIDE = true;

    /**
     * If {@link #AUTO_HIDE} is set, the number of milliseconds to wait after
     * user interaction before hiding the system UI.
     */
    private static final int AUTO_HIDE_DELAY_MILLIS = 3000;

    /**
     * If set, will toggle the system UI visibility upon interaction. Otherwise,
     * will show the system UI visibility upon interaction.
     */
    private static final boolean TOGGLE_ON_CLICK = true;

    /**
     * The flags to pass to {@link SystemUiHider#getInstance}.
     */
    private static final int HIDER_FLAGS = SystemUiHider.FLAG_HIDE_NAVIGATION;

    /**
     * The instance of the {@link SystemUiHider} for this activity.
     */
    private SystemUiHider mSystemUiHider;

    private String id_refugio;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_login);

        id_refugio = this.getIntent().getStringExtra(MainActivity.ID_REFUGIO);

        final View controlsView = findViewById(R.id.fullscreen_content_controls);
        final View contentView = findViewById(R.id.fullscreen_content);

        // Set up an instance of SystemUiHider to control the system UI for
        // this activity.
        mSystemUiHider = SystemUiHider.getInstance(this, contentView, HIDER_FLAGS);
        mSystemUiHider.setup();
        mSystemUiHider
                .setOnVisibilityChangeListener(new SystemUiHider.OnVisibilityChangeListener() {
                    // Cached values.
                    int mControlsHeight;
                    int mShortAnimTime;

                    @Override
                    @TargetApi(Build.VERSION_CODES.HONEYCOMB_MR2)
                    public void onVisibilityChange(boolean visible) {
                        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.HONEYCOMB_MR2) {
                            // If the ViewPropertyAnimator API is available
                            // (Honeycomb MR2 and later), use it to animate the
                            // in-layout UI controls at the bottom of the
                            // screen.
                            if (mControlsHeight == 0) {
                                mControlsHeight = controlsView.getHeight();
                            }
                            if (mShortAnimTime == 0) {
                                mShortAnimTime = getResources().getInteger(
                                        android.R.integer.config_shortAnimTime);
                            }
                            controlsView.animate()
                                    .translationY(visible ? 0 : mControlsHeight)
                                    .setDuration(mShortAnimTime);
                        } else {
                            // If the ViewPropertyAnimator APIs aren't
                            // available, simply show or hide the in-layout UI
                            // controls.
                            controlsView.setVisibility(visible ? View.VISIBLE : View.GONE);
                        }


                    }
                });

        final Button dummybutton = (Button) findViewById(R.id.dummy_button);
        dummybutton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                memoria();
            }
        });


    }

    void memoria(){
        Gson gson = new Gson();

        EditText textUser = (EditText) findViewById(R.id.editText25);
        String user = textUser.getText().toString();

        EditText textPass = (EditText) findViewById(R.id.editText24);
        String password = textPass.getText().toString();



        Map<String, Object> data = new HashMap<String, Object>();
        data.put( "username", user );
        data.put( "password", password );
        data.put( "refugio", Integer.parseInt(id_refugio) );

        String json = gson.toJson(data);

        //Enviarlos al servidor
        RefugioAPIClient.post("api/login", null, json, new JsonHttpResponseHandler() {
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONArray response) {
                String token = response.toString();
                token = token.substring(2,token.length()-2);
                RefugioAPIClient.setTOKEN(token);
                obtenerActividadesRefugio();

            }

            @Override
            public void onFailure(int i, Header[] headers, String bytes, Throwable throwable) {

            }

        });

    }

    private void obtenerActividadesRefugio(){
        RefugioAPIClient.get("api/actividades", null, new JsonHttpResponseHandler() {
            @Override
            public void onStart() {
                super.onStart();
            }


            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONArray response) {
                super.onSuccess(statusCode, headers, response);
                Gson gson = new Gson();
                List<Actividad> actividades = gson.fromJson(response.toString(), new TypeToken<List<Actividad>>() {
                }.getType());
                try {
                    Dao actDao = getHelper().getActividadDao();
                    Dao ejDao = getHelper().getEjercicioDao();
                    for (Actividad a : actividades) {
                        actDao.create(a);
                        for (Ejercicio ej : a.getEjercicios()) {
                            ej.setActividad(a);
                            ejDao.create(ej);
                        }
                    }
                    Intent intent = new Intent(LoginActivity.this, BuscarEjercicioActivity.class);
                    startActivity(intent);
                    finish();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, String responseString, Throwable throwable) {
                super.onFailure(statusCode, headers, responseString, throwable);
            }
        });
    }




}

