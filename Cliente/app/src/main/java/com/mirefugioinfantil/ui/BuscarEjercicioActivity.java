package com.mirefugioinfantil.ui;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;

import com.mirefugioinfantil.R;
import com.mirefugioinfantil.modelo.Actividad;
import com.mirefugioinfantil.modelo.Ejercicio;
import com.mirefugioinfantil.modelo.IdentificadorNFC;

import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;

public class BuscarEjercicioActivity extends DBHandlerNFCActivity{

    public static final String ID_ACTIVIDAD = "com.mirefugioinfantil.id_actividad";
    private static final String ACTIVIDAD = "com.mirefugioinfantil.actividad";
    private static final String ULTIMO_EJERCICIO = "com.mirefugioinfantil.ultimo_ejercicio";
    private static final String ESTADO_ACTIVIDAD = "com.mirefugioinfantil.estado_actividad";
    private Actividad actividad;
    private Integer ultimo_enunciado=0;
    private Map<Integer,Integer> estado_actividad;
    private TextView tView;

    public final static String EJERCICIO = "com.mirefugioinfantil.ejercicio";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //setContentView(R.layout.activity_buscar_enunciado);
        estado_actividad = new HashMap<Integer, Integer>();
        tView = (TextView) findViewById(R.id.fullscreen_content);
        tView.setText("BUSCA ACTIVIDAD");
    }

    private void cargarActividad(Integer id_actividad){
        if(actividad == null || !actividad.getId().equals(id_actividad)) {
            ultimo_enunciado= estado_actividad.containsKey(id_actividad) ? estado_actividad.get(id_actividad) : 0;
            try {
                actividad = getHelper().getActividadDao().queryForId(id_actividad);
                /*QueryBuilder<Actividad, Integer> actividadQb = getHelper().getActividadDao().queryBuilder();
                actividadQb.where().eq(Actividad.ID, id_actividad);
                QueryBuilder<Ejercicio, Integer> ejercicioQb = getHelper().getEjercicioDao().queryBuilder();
                actividad.setEjercicios(ejercicioQb.join(actividadQb).query());*/
            } catch (SQLException e) {
                e.printStackTrace();
            }
        } else {
            /*Reiniciamos contador puesto que lo consideramos como un reset
              es decir, el niño buscará repetir la actividad desde el principio (el primer ejercicio)*/
            ultimo_enunciado = 0;
        }
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState) {
        super.onRestoreInstanceState(savedInstanceState);
        actividad = savedInstanceState.getParcelable(ACTIVIDAD);
        ultimo_enunciado = savedInstanceState.getInt(ULTIMO_EJERCICIO);
        estado_actividad = (Map<Integer, Integer>) savedInstanceState.getSerializable(ESTADO_ACTIVIDAD);
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        outState.putParcelable(ACTIVIDAD,actividad);
        outState.putInt(ULTIMO_EJERCICIO,ultimo_enunciado);
        outState.putSerializable(ESTADO_ACTIVIDAD, (java.io.Serializable) estado_actividad);
        super.onSaveInstanceState(outState);
    }

    @Override
    public void onNFCReceived(String datosNFC) {
        super.onNFCReceived(datosNFC);
        String[] datosNFCsplit = datosNFC.split(IdentificadorNFC.SEPARADOR);
        if(datosNFCsplit[0].equalsIgnoreCase(IdentificadorNFC.SELECCIONAR_EJERCICIO) && actividad!=null) {
            //Pasa a un enunciado activo
            if(ultimo_enunciado<actividad.getEjercicios().size()) {
                Ejercicio activo = (Ejercicio) actividad.getEjercicios().toArray()[ultimo_enunciado++];
                estado_actividad.put(actividad.getId(),ultimo_enunciado);
                Intent intent = new Intent(this, activo.getSiguienteActivity());
                intent.putExtra(ID_ACTIVIDAD, actividad.getId());
                intent.putExtra(EJERCICIO, activo);
                startActivity(intent);
            } else {
                tView.setText("NO HAY MAS EJERCICIOS");
            }
        }
        else if(datosNFCsplit[0].equalsIgnoreCase(IdentificadorNFC.SELECCIONAR_ACTIVIDAD)){
            cargarActividad(Integer.parseInt(datosNFCsplit[1]));
            tView.setText("BUSCA EJERCICIO");
        }
    }

}
