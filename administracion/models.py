from django.db import models
from django.contrib.auth.models import User 
class Recurso(models.Model):
	direccion = models.CharField(max_length=255)
	#Provisionalmente esto es una direccion web de un recurso que puede ser sonido, imagen, etc
	#Otra posibilidad puede ser almacenar un campo tipo y que en vez de recurso se envie directamente el archivo correspondiente al enunciado	
	def __unicode__(self):
		return self.direccion

class Ejercicio(models.Model):
	FACIL = 0
	NORMAL = 1
	DIFICIL = 2
	DIFICULTAD_CHOICES =(
		(FACIL,'Facil'),
		(NORMAL,'Normal'),
		(DIFICIL,'Dificil'),
		)
	UNICA = 0 
	MULTIPLE = 1
	TIPO_RESPUESTA = (
		(UNICA,'Unica'),
		(MULTIPLE,'Multiple'),
		)
	NFC = 0
	ACEL = 1
	TIPO = (
		(NFC,'NFC'),
		(ACEL,'Movimiento'),
		) 
	pregunta = models.CharField(max_length=255)
	solucion = models.CharField(max_length=20)#Array de bits que la posicion corresponde al identificador de un NFC
	tipo_respuesta = models.PositiveSmallIntegerField(choices=TIPO_RESPUESTA,default=UNICA)
	recursos = models.ManyToManyField(Recurso,blank=True,null=True)
	dificultad = models.CharField(max_length=10,choices=DIFICULTAD_CHOICES,default=NORMAL,null=True)
	tipo = models.PositiveSmallIntegerField(choices=TIPO,default=NFC)
	edad_minima = models.PositiveSmallIntegerField(blank=True,null=True)
	edad_maxima = models.PositiveSmallIntegerField(blank=True,null=True)


	def __unicode__(self):
		return self.pregunta 

class Actividad(models.Model):
	nombre = models.CharField(max_length=255)
	ejercicios = models.ManyToManyField(Ejercicio,null=True)#Permite que una actividad no tenga ningun enunciado hasta que el usuario se la asigne

	def __unicode__(self):
		return self.nombre

class Jugador(models.Model):
	user = models.ForeignKey(User)
	fecha_nacimiento = models.DateField()

	def __unicode__(self):
		return self.user.username

class Refugio(models.Model):
	localizacion = models.CharField(max_length=255)
	actividades = models.ManyToManyField(Actividad)
	
	def __unicode__(self):
		return self.localizacion

class Sesion(models.Model):
	jugador = models.ForeignKey(Jugador)
	refugio = models.ForeignKey(Refugio)
	inicio = models.DateTimeField()
	fin = models.DateTimeField(blank=True,null = True)

	def __unicode__(self):
		return "sesion de "+str(self.jugador.user)+" en "+self.refugio.localizacion+" el dia "+str(self.inicio)+" hasta "+str(self.fin)



class Resultado(models.Model):
	sesion = models.ForeignKey(Sesion,related_name='%(app_label)s_%(class)s_resultados')
	actividad = models.ForeignKey(Actividad)
	ejercicio = models.ForeignKey(Ejercicio)
	tiempo_respuesta = models.PositiveIntegerField(default=0)
	respuesta = models.CharField(max_length=20)

	def __unicode__(self):
		return "Resultado para el ejercicio "+str(self.ejercicio.pregunta)#+" en la "+str(self.sesion)

	
		
		