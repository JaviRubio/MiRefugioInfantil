from django.shortcuts import render
from restservice.serializers import ActividadSerializer, ResultadoSerializer
from administracion.models import Actividad, Refugio, Resultado
from rest_framework import generics

#ListAPIView puesto que las actividades solo van a ser consultadas por el dispositivo
class ActividadList(generics.ListAPIView):
	serializer_class = ActividadSerializer
	
	#TODO: Filtrar por edad y dificultad del jugador
	def get_queryset(self):
		actividades = Actividad.objects.filter(refugio__pk=self.kwargs['refugio'])
		return actividades

class ResultadoList(generics.ListCreateAPIView):
	
	serializer_class = ResultadoSerializer

	#Se sobreescribe esta funcion para permitir que el serializador deserialice multiples objetos
	#ya que se recibe una lista de resultados, para ello se cambia el valor por defecto de many a True
	def get_serializer(self, instance=None, data=None, files=None, many=True, partial=False, allow_add_remove=False):
		return super(ResultadoList,self).get_serializer(instance,data,files,many,partial)