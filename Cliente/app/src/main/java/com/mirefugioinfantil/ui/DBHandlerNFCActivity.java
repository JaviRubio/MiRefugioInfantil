package com.mirefugioinfantil.ui;

import android.os.Bundle;

import com.mirefugioinfantil.database.DBHelper;
import com.j256.ormlite.android.apptools.OpenHelperManager;

public class DBHandlerNFCActivity extends NFCActivity {

    private DBHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    public DBHelper getHelper() {
        if (dbHelper == null) {
            dbHelper = OpenHelperManager.getHelper(this, DBHelper.class);
        }
        return dbHelper;
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (dbHelper != null) {
            OpenHelperManager.releaseHelper();
            dbHelper = null;
        }
    }
}
