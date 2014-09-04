from django import forms
from django.forms import ModelForm
from administracion.models import Refugio,Actividad,Ejercicio


class RefugioForm(ModelForm):

	localizacion = forms.CharField(label='Localizacion',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	actividades = forms.ModelMultipleChoiceField(label='Actividades',queryset=Actividad.objects.all(), widget=forms.SelectMultiple(attrs={'class':'main-box clearfix'}))
	class Meta:
		model = Refugio
		fields = ['localizacion','actividades']

class ActividadForm(ModelForm):

	nombre = forms.CharField(label='Nombre',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	ejercicios = forms.ModelMultipleChoiceField(label='Ejercicios',queryset=Ejercicio.objects.all(), widget=forms.SelectMultiple(attrs={'class':'main-box clearfix'}))
	class Meta:
		model = Actividad
		fields = ['nombre', 'ejercicios']

class EjercicioForm(ModelForm):

	pregunta = forms.CharField(label='Pregunta',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	solucion = forms.CharField(label='Solucion',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
	tipo_respuesta = forms.TypedChoiceField(label='Tipo respuesta',choices=Ejercicio.TIPO_RESPUESTA,widget=forms.Select(attrs={'class': 'form-control'}))
	dificultad = forms.TypedChoiceField(label='Dificultad',choices=Ejercicio.DIFICULTAD_CHOICES,widget=forms.Select(attrs={'class': 'form-control'}))
	tipo = forms.TypedChoiceField(label='Tipo ejercicio',choices=Ejercicio.TIPO,widget=forms.Select(attrs={'class': 'form-control'}))
	edad_minima = forms.TypedChoiceField(label='Edad minima',widget=forms.NumberInput(attrs={'class': 'form-control'}))
	edad_maxima = forms.TypedChoiceField(label='Edad maxima',widget=forms.NumberInput(attrs={'class': 'form-control'}))
	class Meta:
		model = Ejercicio
		fields = ['pregunta', 'solucion', 'tipo_respuesta', 'dificultad', 'tipo', 'edad_minima', 'edad_maxima']