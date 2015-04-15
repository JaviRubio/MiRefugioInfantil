package com.mirefugioinfantil.database;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;

import com.mirefugioinfantil.modelo.Jugador;
import com.j256.ormlite.android.apptools.OrmLiteSqliteOpenHelper;
import com.j256.ormlite.dao.Dao;
import com.j256.ormlite.support.ConnectionSource;
import com.j256.ormlite.table.TableUtils;
import com.mirefugioinfantil.modelo.Actividad;
import com.mirefugioinfantil.modelo.Ejercicio;
import com.mirefugioinfantil.modelo.Resultado;


import java.sql.SQLException;

/**
 * Created by cristianmp on 14/08/14.
 */
public class DBHelper extends OrmLiteSqliteOpenHelper {

    private static final String DATABASE_NAME = "mirefugioinfantil.db";
    private static final int DATABASE_VERSION = 1;

    private Dao<Actividad,Integer> actividadDao;
    private Dao<Ejercicio,Integer> ejercicioDao;
    private Dao<Resultado,Integer> resultadoDao;
    private Dao<Jugador,String> jugadorDao;

    public DBHelper(Context context){
        super(context,DATABASE_NAME,null,DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase, ConnectionSource connectionSource) {
        try {
            TableUtils.createTable(connectionSource, Actividad.class);
            TableUtils.createTable(connectionSource, Ejercicio.class);
            TableUtils.createTable(connectionSource, Resultado.class);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, ConnectionSource connectionSource, int i, int i2) {
        onCreate(sqLiteDatabase,connectionSource);
    }

    public Dao<Actividad,Integer> getActividadDao() throws SQLException {
        if(actividadDao == null){
            actividadDao = getDao(Actividad.class);
        }
        return actividadDao;
    }

    public Dao<Ejercicio,Integer> getEjercicioDao() throws SQLException{
        if(ejercicioDao == null){
            ejercicioDao = getDao(Ejercicio.class);
        }
        return ejercicioDao;
    }

    public Dao<Resultado,Integer> getResultadoDao() throws SQLException {
        if(resultadoDao == null){
            resultadoDao = getDao(Resultado.class);
        }
        return resultadoDao;
    }

    public Dao<Jugador,String> getJugadorDao() throws SQLException {
        if(jugadorDao == null){
            jugadorDao = getDao(Jugador.class);
        }
        return jugadorDao;
    }

    @Override
    public void close() {
        super.close();
        actividadDao = null;
        ejercicioDao = null;
        resultadoDao = null;
        jugadorDao = null;
    }
}
