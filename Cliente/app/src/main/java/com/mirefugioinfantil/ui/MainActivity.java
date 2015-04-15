package com.mirefugioinfantil.ui;

import com.mirefugioinfantil.R;
import com.mirefugioinfantil.modelo.IdentificadorNFC;
import com.mirefugioinfantil.ui.util.SystemUiHider;

import android.content.Intent;
import android.os.Bundle;
import android.widget.TextView;


/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 *
 * @see SystemUiHider
 */
public class MainActivity extends DBHandlerNFCActivity {

    public final static String ID_REFUGIO = "com.mirefugioinfantil.id_refugio";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        TextView tView = (TextView) findViewById(R.id.fullscreen_content);
        tView.setText("BUSCA LLAVE DEL REFUGIO");

    }

    @Override
    public void onNFCReceived(String datosNFC) {
        super.onNFCReceived(datosNFC);
        //LEER EL NFC DE LA LLAVE
        String[] datosNFCsplit = datosNFC.split(IdentificadorNFC.SEPARADOR);
        if(datosNFCsplit[0].equalsIgnoreCase(IdentificadorNFC.LLAVE_REFUGIO)){


            Intent intent = new Intent(this, LoginActivity.class);
            intent.putExtra(ID_REFUGIO, datosNFCsplit[1]);
            startActivity(intent);

            finish();
        }
    }


}
