package com.mirefugioinfantil.modelo;

/**
 * Created by vicenteabadrodriguez on 12/08/14.
 */
public class IdentificadorNFC {

    /**
     * SELECCIONAR EJERCICIO = 0
     * LLAVE REFUGIO = 1_IDREFUGIO
     * SELECCIONAR ACTIVIDAD = 2_IDACTIVIDAD
     * ITEMS ACTIVIDAD = 3_(IDACTIVIDAD:POSICIONITEM)+
     * FIN = 404
     */

    public static final String SEPARADOR = "_";
    public static final String SEPARADOR_ITEM = ":";
    public static final String SELECCIONAR_EJERCICIO = "0";
    public static final String LLAVE_REFUGIO = "1";
    public static final String SELECCIONAR_ACTIVIDAD = "2";
    public static final String ITEM_ACTIVIDAD = "3";
    public static final String FIN = "404";

}
