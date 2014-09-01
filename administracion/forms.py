from django import forms
from django.forms import ModelForm
from administracion.models import Refugio

class RefugioForm(ModelForm):

	localizacion = forms.CharField(label='Localizacion',max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Refugio
		fields = ['localizacion']