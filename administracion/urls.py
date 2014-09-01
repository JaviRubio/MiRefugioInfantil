from django.conf.urls import patterns, include, url
from administracion.views import RefugioListView, RefugioDetailView, RefugioCreate, RefugioUpdate, RefugioDelete, ActividadListView, ActividadDetailView, EjercicioListView, EjercicioDetailView 
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$','administracion.views.get_principal'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^refugios/nuevo', RefugioCreate.as_view(),name='crear_refugio'),
    url(r'^refugios/editar/(?P<pk>\d+)/',RefugioUpdate.as_view(),name='editar_refugio'),
    url(r'^refugios/borrar/(?P<pk>\d+)/',RefugioDelete.as_view(),name='borrar_refugio'),
    url(r'^refugios/(?P<pk>\d+)',RefugioDetailView.as_view(),name='detalle_refugio'),
    url(r'^refugios/',RefugioListView.as_view(),name='lista_refugios'),
    url(r'^ejercicios/(?P<pk>\d+)',EjercicioDetailView.as_view(), name='detalle_enunciado'),
    url(r'^ejercicios/',EjercicioListView.as_view(), name='lista_enunciados'),
    url(r'^actividades/(?P<pk>\d+)',ActividadDetailView.as_view(), name='detalle_actividad'),
    url(r'^actividades/',ActividadListView.as_view(), name='lista_actividades'),    
)