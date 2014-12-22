import datetime
import json
from django.shortcuts import render, get_object_or_404
from restservice import serializers
from administracion.models import Actividad, Refugio, Resultado, Sesion,Jugador
from rest_framework import generics,mixins,views,response,status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#A traves del token de autenticacion se obtiene la sesion que contiene el refugio desde donde se pide la lista de actividades
#ListAPIView puesto que las actividades solo van a ser consultadas por el dispositivo
class ActividadList(generics.ListAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	serializer_class = serializers.ActividadSerializer
	
	#TODO: Filtrar por edad y dificultad del jugador
	def get_queryset(self):
		sesion = Sesion.objects.get(jugador__user=self.request.user,fin__isnull=True)
		actividades = Actividad.objects.filter(refugio=sesion.refugio)
		return actividades

#Cuando se sale del refugio se llama a esta vista,
#para actualizar la hora de fin de la sesion y borrar el token
class LogoutView(views.APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self,request,format=None):
		token = Token.objects.get(user=request.user)
		Sesion.objects.filter(jugador__user=request.user,fin__isnull=True).update(fin=datetime.datetime.now())
		token.delete()
		return response.Response()

#Se envian los resultados para una sesion determinada, por ello se autentica mediante token
class ResultadoList(generics.ListCreateAPIView):
	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	serializer_class = serializers.ResultadoSerializer

	#Se sobreescribe esta funcion para permitir que el serializador deserialice multiples objetos
	#ya que se recibe una lista de resultados, para ello se cambia el valor por defecto de many a True
	def get_serializer(self, instance=None, data=None, files=None, many=True, partial=False, allow_add_remove=False):
		return super(ResultadoList,self).get_serializer(instance,data,files,many,partial)

#Se comprueba que los datos de entrada son correctos y se crea una sesion en el refugio correspondiente,
#ademas se crea un token para identificar a ese jugador durante toda la sesion
class LoginJugadorAPIView(views.APIView):

	def post(self, request, format=None):
		serializer = serializers.LoginJugadorSerializer(data=request.DATA)
		if serializer.is_valid():
			jugador = get_object_or_404(Jugador.objects.filter(user__username=serializer.object['username']))
			if jugador.user.check_password(serializer.object['password']):
				token,created = Token.objects.get_or_create(user=jugador.user)
				if created:
					ref = Refugio.objects.get(pk=serializer.object['refugio'])
					sesion = Sesion(jugador=jugador,refugio=ref,inicio=datetime.datetime.now(),fin=None)
					sesion.save()
					return response.Response(data={token.key})
		return response.Response(status=status.HTTP_400_BAD_REQUEST)



