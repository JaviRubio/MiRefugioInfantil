package com.mirefugioinfantil.ui;

import com.mirefugioinfantil.modelo.IdentificadorNFC;

import android.app.Activity;
import android.app.PendingIntent;
import android.content.Intent;
import android.content.IntentFilter;
import android.nfc.NfcAdapter;
import android.nfc.Tag;
import android.os.Bundle;

public class NFCActivity extends BaseActivity implements NFCReader.ManejadorNFC {

    private NfcAdapter miNfcAdapter;
    public static final String MIME_TEXT_PLAIN = "text/plain";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        miNfcAdapter = NfcAdapter.getDefaultAdapter(this);
    }


    public static void setupForegroundDispatch(final Activity activity, NfcAdapter adapter) {
        final Intent intent = new Intent(activity.getApplicationContext(), activity.getClass());
        intent.setFlags(Intent.FLAG_ACTIVITY_SINGLE_TOP);

        final PendingIntent pendingIntent = PendingIntent.getActivity(activity.getApplicationContext(), 0, intent, 0);

        IntentFilter[] filters = new IntentFilter[3];
        String[][] techList = new String[][]{};

        // Notice that this is the same filter as in our manifest.
        filters[0] = new IntentFilter();
        filters[0].addAction(NfcAdapter.ACTION_NDEF_DISCOVERED);
        filters[0].addCategory(Intent.CATEGORY_DEFAULT);
        try {
            filters[0].addDataType(MIME_TEXT_PLAIN);
        } catch (IntentFilter.MalformedMimeTypeException e) {
            throw new RuntimeException("Check your mime type.");
        }
        filters[1] = new IntentFilter();
        filters[1].addAction(NfcAdapter.ACTION_TECH_DISCOVERED);

        filters[2] = new IntentFilter();
        filters[2].addAction(NfcAdapter.ACTION_TAG_DISCOVERED);

        adapter.enableForegroundDispatch(activity, pendingIntent, filters, techList);
    }

    @Override
    protected void onResume() {
        super.onResume();
        setupForegroundDispatch(this, miNfcAdapter);
    }

    @Override
    protected void onPause() {
        stopForegroundDispatch(this, miNfcAdapter);
        super.onPause();
    }

    public static void stopForegroundDispatch(final Activity activity, NfcAdapter adapter) {
        adapter.disableForegroundDispatch(activity);
    }

    @Override
    protected void onNewIntent(Intent intent) {
        handleIntent(intent);

    }

    private void handleIntent(Intent intent) {
        if(NfcAdapter.ACTION_NDEF_DISCOVERED.equals(intent.getAction())) {
            new NFCReader(this).execute((Tag)intent.getParcelableExtra(NfcAdapter.EXTRA_TAG));
        }
    }


    @Override
    public void onNFCReceived(String datosNFC) {
        if (datosNFC.equalsIgnoreCase(IdentificadorNFC.FIN)) {
            startActivity(new Intent(this,FinActivity.class));
            this.finish();
        }

    }
}
