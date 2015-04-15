package com.mirefugioinfantil.modelo;

import android.os.Parcel;
import android.os.Parcelable;

import com.google.gson.annotations.Expose;
import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.field.ForeignCollectionField;
import com.j256.ormlite.table.DatabaseTable;

import java.util.Arrays;
import java.util.Collection;

/**
 * Created by vicenteabadrodriguez on 11/08/14.
 */
@DatabaseTable
public class Actividad implements Parcelable{

    public static final String ID = "_id";
    public static final String NOMBRE = "nombre";
    public static final String EJERCICIO ="ejercicios";

    @Expose
    @DatabaseField(id=true, columnName = ID)
    private Integer id;

    @Expose(serialize = false)
    @DatabaseField(columnName = NOMBRE)
    private String nombre;

    @Expose(serialize = false)
    @ForeignCollectionField(columnName = EJERCICIO)
    private Collection<Ejercicio> ejercicios;

    public Actividad() {
    }

    public Actividad(Integer id) {
        this.id = id;
    }

    public Actividad(Parcel parcel) {
        this.readFromParcel(parcel);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Collection<Ejercicio> getEjercicios() {
        return ejercicios;
    }

    public void setEjercicios(Collection<Ejercicio> ejercicios) {
        this.ejercicios = ejercicios;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel parcel, int i) {
        parcel.writeInt(id);
        parcel.writeString(nombre);
        parcel.writeList(Arrays.asList(ejercicios.toArray()));
    }


    public void readFromParcel(Parcel parcel){
        id = parcel.readInt();
        nombre = parcel.readString();
        ejercicios = parcel.readArrayList(Ejercicio.class.getClassLoader());
    }

    public static final Creator<Actividad> CREATOR = new Creator<Actividad>() {
        @Override
        public Actividad createFromParcel(Parcel parcel) {
            return new Actividad(parcel);
        }

        @Override
        public Actividad[] newArray(int i) {
            return new Actividad[i];
        }

    };

}
