from django.shortcuts import render, render_to_response, get_object_or_404
#from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from administracion.models import Refugio, Actividad, Ejercicio
from administracion.forms import RefugioForm, ActividadForm

#def es_grupo_usuario(user,nombre_grupo):
	#return user.groups.filter(name=nombre_grupo)
#	pass

#@user_passes_test(lambda u: es_grupo_usuario(u, "admin"))
#@user_passes_test(lambda u: es_grupo_usuario(u, "admin_refugio"))
#@user_passes_test(lambda u: es_grupo_usuario(u, "jugador"))
#def prueba(request):
#	pass

@login_required(login_url='login')
def get_principal(request):
	return render(request,"administracion/index.html")


class RefugioListView(ListView):

	context_object_name = "lista_refugios"
	queryset = Refugio.objects.all()
	template_name = "administracion/refugios.html"


class RefugioDetailView(DetailView):

	model = Refugio
	context_object_name = "detalle_refugio"
	template_name = "administracion/refugio.html"

class RefugioCreate(CreateView):
	model = Refugio
	form_class = RefugioForm
	success_url = reverse_lazy('lista_refugios')
	template_name = 'administracion/nuevo_refugio.html'

class RefugioUpdate(UpdateView):
	model = Refugio
	form_class = RefugioForm
	success_url = reverse_lazy('lista_refugios')
	template_name = 'administracion/editar_refugio.html'

class RefugioDelete(DeleteView):
	model = Refugio
	success_url = reverse_lazy('lista_refugios')
	#template_name = 'administracion/borrar_refugio.html'

class ActividadListView(ListView):

	context_object_name = "lista_actividades"
	queryset = Actividad.objects.all()
	template_name = "administracion/actividades.html"

class ActividadDetailView(DetailView):

	model = Actividad
	context_object_name = "detalle_actividad"
	template_name = "administracion/actividad.html"


class ActividadCreate(CreateView):
	model = Actividad
	form_class = ActividadForm
	success_url = reverse_lazy('lista_actividades')
	template_name = 'administracion/nuevo_actividad.html'

class ActividadUpdate(UpdateView):
	model = Actividad
	form_class = ActividadForm
	success_url = reverse_lazy('lista_actividades')
	template_name = 'administracion/editar_actividad.html'

class ActividadDelete(DeleteView):
	model = Actividad
	success_url = reverse_lazy('lista_actividades')
	#template_name = 'administracion/borrar_refugio.html'	

#Muestra todos los ejercicios de una actividad
class EjercicioListView(ListView):

	context_object_name = "lista_enunciados"
	queryset = Ejercicio.objects.all()
	template_name = "administracion/vincular_enunciado.html"


class EjercicioDetailView(DetailView):

	model = Ejercicio
	context_object_name = "detalle_enunciado"
	template_name = "administracion/enunciado.html"



