from administracion.models import Actividad,Ejercicio,Recurso, Sesion, Resultado
from rest_framework import serializers

class RecursoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recurso
		fields = ['direccion']

class EjercicioSerializer(serializers.ModelSerializer):
	recursos = RecursoSerializer(many=True)

	class Meta:
		model = Ejercicio
		fields = ('id','tipo','pregunta','solucion','tipo_respuesta','recursos')

class ActividadSerializer(serializers.ModelSerializer):
	ejercicios = EjercicioSerializer(many=True)

	class Meta:
		model = Actividad
		fields = ('id','nombre','ejercicios')

class SesionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sesion

class ResultadoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Resultado
		
