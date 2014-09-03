from django import forms
from django.forms import ModelForm
from administracion.models import Refugio,Actividad,Ejercicio


class RefugioForm(ModelForm):

	localizacion = forms.CharField(label='Localizacion',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Refugio
		fields = ['localizacion']

class ActividadForm(ModelForm):

	nombre = forms.CharField(label='Nombre',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	ejercicios = forms.ModelMultipleChoiceField(label='Ejercicios',queryset=Ejercicio.objects.all(),widget=forms.SelectMultiple(attrs={'id':'ejercicios_list','class':'main-box clearfix'}))
	class Meta:
		model = Actividad
		fields = ['nombre', 'ejercicios']

class EjercicioForm(ModelForm):

	pregunta = forms.CharField(label='Pregunta',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = Ejercicio
		fields = ['pregunta']
		