package com.mirefugioinfantil.modelo;

import com.j256.ormlite.field.DatabaseField;
import com.j256.ormlite.table.DatabaseTable;

/**
 * Created by vicenteabadrodriguez on 19/09/14.
 */

@DatabaseTable
public class Jugador{

    public static final String USUARIO = "usuario";
    public static final String PASSWORD = "password";

    @DatabaseField(id=true, columnName = USUARIO)
    private String usuario;

    @DatabaseField(columnName = PASSWORD)
    private String password;

    public Jugador() {

    }

    public Jugador(String usuario, String password) {
        this.usuario = usuario;
        this.password = password;
    }

    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
