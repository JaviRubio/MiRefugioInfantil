from django.conf.urls import patterns, include, url
from restservice.views import ActividadList, ResultadoList

urlpatterns = patterns('',
      url(r'^api/actividades/(?P<refugio>\d+)',ActividadList.as_view()),
      url(r'^api/resultados', ResultadoList.as_view()),
)
