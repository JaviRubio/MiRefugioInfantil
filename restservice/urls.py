from django.conf.urls import patterns, include, url
from restservice.views import ActividadList, ResultadoList, LoginJugadorAPIView, LogoutView

urlpatterns = patterns('',
      url(r'^api/actividades/',ActividadList.as_view()),
      url(r'^api/login',LoginJugadorAPIView.as_view()),
      url(r'^api/logout',LogoutView.as_view()),
      url(r'^api/resultados', ResultadoList.as_view()),
)
