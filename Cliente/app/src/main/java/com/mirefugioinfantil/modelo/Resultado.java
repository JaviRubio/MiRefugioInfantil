package com.mirefugioinfantil.modelo;

import com.google.gson.annotations.Expose;
import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.table.DatabaseTable;

/**
 * Created by vicenteabadrodriguez on 11/08/14.
 */

@DatabaseTable
public class Resultado{

    public static final String VALOR_RESULTADO="valor_resultado";
    private static final String TIEMPO_RESPUESTA = "tiempo_respuesta";
    private static final String SEPARADOR = ";";

    @Expose(serialize = false, deserialize = false)
    @DatabaseField(id =true)
    private Integer id;

    @Expose
    @DatabaseField(columnName = VALOR_RESULTADO)
    private String respuesta = "";

    @Expose
    @DatabaseField(columnName = TIEMPO_RESPUESTA)
    private long tiempo_respuesta;

    @Expose
    @DatabaseField //Solo para la BBDD no se usa en esta clase
    private Integer ejercicio;

    @Expose
    @DatabaseField
    private Integer actividad;

    public Resultado() {
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getRespuesta() {
        return respuesta;
    }

    public void setRespuesta(String respuesta) {
        this.respuesta = respuesta;
    }

    public Integer getEjercicio() {
        return ejercicio;
    }

    public void setEjercicio(Integer ejercicio) {
        this.ejercicio = ejercicio;
    }

    public long getTiempo_respuesta() {
        return tiempo_respuesta;
    }

    public void setTiempo_respuesta(long tiempo_respuesta) {
        this.tiempo_respuesta = tiempo_respuesta;
    }

    public Integer getActividad() {
        return actividad;
    }

    public void setActividad(Integer actividad) {
        this.actividad = actividad;
    }

    public void actualizarResultado(String cod){
        respuesta = respuesta.concat(cod+SEPARADOR);
    }

    public Boolean estaIncluida(String valor) {
        for (String s : respuesta.split(SEPARADOR))
            if(s.equalsIgnoreCase(valor))
                return true;
        return false;
    }

}
