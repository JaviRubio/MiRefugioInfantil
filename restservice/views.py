import datetime
from django.shortcuts import render, get_object_or_404
from restservice import serializers
from administracion.models import Actividad, Refugio, Resultado, Sesion,Jugador
from rest_framework import generics,mixins,views,response,status

#ListAPIView puesto que las actividades solo van a ser consultadas por el dispositivo
class ActividadList(generics.ListAPIView):
	serializer_class = serializers.ActividadSerializer
	
	#TODO: Filtrar por edad y dificultad del jugador
	def get_queryset(self):
		actividades = Actividad.objects.filter(refugio__pk=self.kwargs['refugio'])
		return actividades

#Cuando se sale del refugio se llama a esta vista,
# para actualizar la hora de fin de la sesion y obtener la id para incluirla en el array de resultados que se invocaran

#Mirar el viewset
class SesionAPIView(mixins.UpdateModelMixin,generics.RetrieveAPIView):
	
	serializer_class = serializers.SesionSerializer
	queryset = Sesion.objects.all()

	def put(self,request, *args, **kwargs):
		return self.partial_update(request,args,kwargs)

	def get_serializer(self, instance=None, data=None, files=None,many=False, partial=True, allow_add_remove=False):
		return super(SesionAPIView,self).get_serializer(instance,self.request.DATA,files,many,partial)

class ResultadoList(generics.ListCreateAPIView):
	
	serializer_class = serializers.ResultadoSerializer

	#Se sobreescribe esta funcion para permitir que el serializador deserialice multiples objetos
	#ya que se recibe una lista de resultados, para ello se cambia el valor por defecto de many a True
	def get_serializer(self, instance=None, data=None, files=None, many=True, partial=False, allow_add_remove=False):
		return super(ResultadoList,self).get_serializer(instance,data,files,many,partial)

class LoginJugadorAPIView(views.APIView):

	def post(self, request, format=None):
		print(request.user)
		serializer = serializers.LoginJugadorSerializer(data=request.DATA)
		if serializer.is_valid():
			jugador = get_object_or_404(Jugador.objects.filter(user__username=serializer.object['username']))
			if jugador.user.check_password(serializer.object['password']):
				ref = Refugio.objects.get(pk=serializer.object['refugio'])
				sesion = Sesion(jugador=jugador,refugio=ref,inicio=datetime.datetime.now(),fin=None)
				sesion.save()
				return response.Response()
		return response.Response(status=status.HTTP_400_BAD_REQUEST)



