from administracion import models
from rest_framework import serializers

class RecursoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Recurso
		fields = ['direccion']

class EjercicioSerializer(serializers.ModelSerializer):
	recursos = RecursoSerializer(many=True)

	class Meta:
		model = models.Ejercicio
		fields = ('id','tipo','pregunta','solucion','tipo_respuesta','recursos')

class ActividadSerializer(serializers.ModelSerializer):
	ejercicios = EjercicioSerializer(many=True)

	class Meta:
		model = models.Actividad
		fields = ('id','nombre','ejercicios')

class ResultadoSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Resultado

class SesionSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Sesion
		fields= ['id']

class LoginJugadorSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	refugio = serializers.IntegerField()


		
