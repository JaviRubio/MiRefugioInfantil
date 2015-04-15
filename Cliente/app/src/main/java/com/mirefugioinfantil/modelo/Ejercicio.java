package com.mirefugioinfantil.modelo;

import android.os.Parcel;
import android.os.Parcelable;

import com.mirefugioinfantil.ui.RealizarEjercicioAcelerometro;
import com.mirefugioinfantil.ui.RealizarEjercicioNFCActivity;
import com.google.gson.annotations.Expose;
import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.table.DatabaseTable;

import java.util.Collection;

/**
 * Created by vicenteabadrodriguez on 11/08/14.
 */
@DatabaseTable
public class Ejercicio implements Parcelable {

    private static class Tipo{
        public static final Integer NFC = 0;
        public static final Integer ACELEROMETRO = 1;
    }

    private static class TipoRespuesta{
        public static final Integer UNICA = 0;
        public static final Integer MULTIPLE = 1;
    }

    public static final String ID = "_id";
    public static final String TIPO = "tipo";
    public static final String PREGUNTA = "pregunta";
    public static final String SOLUCION = "solucion";
    public static final String RECURSO = "recurso";
    public static final String TIPO_RESPUESTA = "tipo_respuesta";

    @Expose
    @DatabaseField(id=true, columnName = ID)
    private Integer id;

    @Expose(serialize = false)
    @DatabaseField(columnName = TIPO)
    private Integer tipo;

    @Expose(serialize = false)
    @DatabaseField(columnName = PREGUNTA)
    private String pregunta;

    @Expose(serialize = false)
    @DatabaseField(columnName = SOLUCION)
    private String solucion;

    @Expose(serialize = false)
    @DatabaseField(columnName = TIPO_RESPUESTA)
    private Integer tipo_respuesta;

    @Expose(serialize = false)
    //@DatabaseField(columnName = RECURSO)
    private Collection<String> recursos; //URL


    //Solo para la BBDD no se usa en esta clase
    @Expose(serialize = false, deserialize = false)
    @DatabaseField(foreign = true)
    private Actividad actividad;

    public Ejercicio(){

    }

    public Ejercicio(Parcel parcel){
        this();
        readFromParcel(parcel);
    }

    public Integer getId() {
        return id;
    }

    public Actividad getActividad() {
        return actividad;
    }

    public void setActividad(Actividad actividad) {
        this.actividad = actividad;
    }

    public String getPregunta() {
        return pregunta;
    }

    public void setPregunta(String pregunta) {
        this.pregunta = pregunta;
    }

    public String getSolucion() {
        return solucion;
    }

    public void setSolucion(String solucion) {
        this.solucion = solucion;
    }

    public Integer getTipo_respuesta() {
        return tipo_respuesta;
    }

    public void setTipo_respuesta(Integer tipo_respuesta) {
        this.tipo_respuesta = tipo_respuesta;
    }

    public Integer getTipo() {
        return tipo;
    }

    public void setTipo(Integer tipo) {
        this.tipo = tipo;
    }

    public Collection<String> getRecursos() {
        return recursos;
    }

    public void setRecursos(Collection<String> recursos) {
        this.recursos = recursos;
    }

    public Class getSiguienteActivity(){

        if(this.tipo == Tipo.NFC) return RealizarEjercicioNFCActivity.class;
        else if(this.tipo == Tipo.ACELEROMETRO) return RealizarEjercicioAcelerometro.class;

        return null;
    }

    public Integer cuantasSoluciones(){
        if(this.tipo_respuesta.equals(TipoRespuesta.MULTIPLE)){
            int contador = 0;
            for(int i=0; i < solucion.length(); i++){
                if(solucion.charAt(i)=='1') contador++;
            }
            return contador;
        }
        else return 1;

    }

    public Boolean esCorrecta(String valor){
        return solucion.charAt(Integer.parseInt(valor))=='1';
    }

    @Override
    public int describeContents() {
        return 0;
    }

    public void readFromParcel(Parcel parcel){
        id = parcel.readInt();
        pregunta = parcel.readString();
        solucion = parcel.readString();
        tipo_respuesta = parcel.readInt();
        tipo = parcel.readInt();
        //recursos = parcel.readString();

    }

    @Override
    public void writeToParcel(Parcel parcel, int i) {
        parcel.writeInt(id);
        parcel.writeString(pregunta);
        parcel.writeString(solucion);
        parcel.writeInt(tipo_respuesta);
        parcel.writeInt(tipo);
        //parcel.writeString(recursos);

    }

    public static final Creator<Ejercicio> CREATOR = new Creator<Ejercicio>() {
        @Override
        public Ejercicio createFromParcel(Parcel parcel) {
            return new Ejercicio(parcel);
        }

        @Override
        public Ejercicio[] newArray(int i) {
            return new Ejercicio[i];
        }
    };

}
