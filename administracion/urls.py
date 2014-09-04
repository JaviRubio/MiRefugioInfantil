from django.conf.urls import patterns, include, url
from administracion import views
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^$login/',include(admin.site.urls),name='login'),
    url(r'^$','administracion.views.get_principal',name='inicio'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^refugios/nuevo', views.RefugioCreate.as_view(),name='crear_refugio'),
    url(r'^refugios/editar/(?P<pk>\d+)/',views.RefugioUpdate.as_view(),name='editar_refugio'),
    url(r'^refugios/borrar/(?P<pk>\d+)/',views.RefugioDelete.as_view(),name='borrar_refugio'),
    url(r'^refugios/(?P<pk>\d+)',views.RefugioDetailView.as_view(),name='detalle_refugio'),
    url(r'^refugios/',views.RefugioListView.as_view(),name='lista_refugios'),
    #url(r'^ejercicios/(?P<pk>\d+)',views.EjercicioDetailView.as_view(), name='detalle_enunciado'),
    #url(r'^ejercicios/',views.EjercicioListView.as_view(), name='lista_enunciados'),
    url(r'^actividades/nuevo', views.ActividadCreate.as_view(),name='crear_actividad'),
    url(r'^actividades/editar/(?P<pk>\d+)/',views.ActividadUpdate.as_view(),name='editar_actividad'),
    url(r'^actividades/borrar/(?P<pk>\d+)/',views.ActividadDelete.as_view(),name='borrar_actividad'),
    url(r'^actividades/(?P<pk>\d+)',views.ActividadDetailView.as_view(), name='detalle_actividad'),
    url(r'^actividades/',views.ActividadListView.as_view(), name='lista_actividades'),
    url(r'^ejercicios/nuevo', views.EjercicioCreate.as_view(),name='crear_ejercicio'),
    url(r'^ejercicios/editar/(?P<pk>\d+)/',views.EjercicioUpdate.as_view(),name='editar_ejercicio'),
    url(r'^ejercicios/borrar/(?P<pk>\d+)/',views.EjercicioDelete.as_view(),name='borrar_ejercicio'),
    url(r'^ejercicios/(?P<pk>\d+)',views.EjercicioDetailView.as_view(),name='detalle_ejercicio'),
    url(r'^ejercicios/',views.EjercicioListView.as_view(),name='lista_ejercicios'),    
)