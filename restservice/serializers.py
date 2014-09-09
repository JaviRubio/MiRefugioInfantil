from administracion import models
from rest_framework import serializers

class RecursoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Recurso
		fields = ('direccion',)

class EjercicioSerializer(serializers.ModelSerializer):
	recursos = RecursoSerializer(many=True)

	class Meta:
		model = models.Ejercicio
		fields = ('id','tipo','pregunta','solucion','tipo_respuesta','recursos')

class ActividadSerializer(serializers.ModelSerializer):
	ejercicios = EjercicioSerializer(many=True) #Flag para activar la [de]serializacion de multiples objetos Ejercicio

	class Meta:
		model = models.Actividad
		fields = ('id','nombre','ejercicios')

#Aunque un objeto Resultado contiene una sesion, no es necesario [de]serializarla, ya que podemos obtenerla a traves del token de autenticacion
#Sin embargo, para poder crear un objeto Resultado se necesita el objeto Sesion, debido a que es una FK, la solucion es acceder a la request
#y obtener el user que ha realizado la peticion y asi, obtener la Sesion
class ResultadoSerializer(serializers.ModelSerializer):

	def restore_object(self, attrs, instance=None):
		assert instance is None, 'No se puede deserializar resultado'
		sesion = models.Sesion.objects.get(jugador__user=self.context['request'].user,fin__isnull=True)
		resultado = models.Resultado(sesion=sesion,actividad=attrs['actividad'],ejercicio=attrs['ejercicio'],tiempo_respuesta=attrs['tiempo_respuesta'],respuesta=attrs['respuesta'])
		return resultado

	class Meta:
		model = models.Resultado
		fields = ('actividad','ejercicio','tiempo_respuesta','respuesta')

#Serializador personalizado, ya que no necesitamos mas para el login de un jugador
class LoginJugadorSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	refugio = serializers.IntegerField()


		
