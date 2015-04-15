package com.mirefugioinfantil.net;


import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.AsyncHttpResponseHandler;
import com.loopj.android.http.RequestParams;

import org.apache.http.entity.StringEntity;

import java.io.UnsupportedEncodingException;

/**
 * Created by vicenteabadrodriguez on 20/08/14.
 */
public class RefugioAPIClient {

    //private static final String BASE_URL = "http://desp32.ugr.es:8000/";

    //IP local para depurar
    private static final String BASE_URL = "http://192.168.1.10:8000/";

    private static AsyncHttpClient client = new AsyncHttpClient();

    public static void get(String url, RequestParams params, AsyncHttpResponseHandler responseHandler ) {

        client.get(getAbsoluteUrl(url), params, responseHandler);
    }

    public static void post(String url, RequestParams params, String jsonString, AsyncHttpResponseHandler responseHandler) {
        StringEntity entity = null;


        try {
            entity = new StringEntity(jsonString);
            client.post(null,getAbsoluteUrl(url),entity,"application/json",responseHandler);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }

    private static String getAbsoluteUrl(String relativeUrl) {
        return BASE_URL + relativeUrl;
    }

    public static void setTOKEN(String TOKEN) {
        client.addHeader("Authorization", "Token " + TOKEN);
    }
}
