from django.shortcuts import render, render_to_response, get_object_or_404
#from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import ContextMixin
from administracion.models import Refugio, Actividad, Ejercicio, Jugador, Resultado
from django.contrib.auth.models import User
from administracion.forms import RefugioForm, ActividadForm, EjercicioForm, EjercicioVincularForm, JugadorForm, JugadorUpdateForm
from django.forms.models import model_to_dict


#def es_grupo_usuario(user,nombre_grupo):
	#return user.groups.filter(name=nombre_grupo)
#	pass

#@user_passes_test(lambda u: es_grupo_usuario(u, "admin"))
#@user_passes_test(lambda u: es_grupo_usuario(u, "admin_refugio"))
#@user_passes_test(lambda u: es_grupo_usuario(u, "jugador"))
#def prueba(request):
#	pass

#@login_required(login_url='login')
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

#Muestra todos los ejercicios de una actividad
class EjercicioListView(ListView):

	context_object_name = "lista_ejercicios"
	queryset = Ejercicio.objects.all()
	template_name = "administracion/ejercicios.html"


class EjercicioDetailView(DetailView):
	model = Ejercicio
	def get_context_data(self, **kwargs):
		context = super(EjercicioDetailView, self).get_context_data(**kwargs)
		context['respuesta'] = self.object.TIPO_RESPUESTA[self.object.tipo_respuesta][1]
		context['tipo_ejercicio'] = self.object.TIPO[self.object.tipo][1]
		#context['form'] = EjercicioVincularForm
		return context

	context_object_name = "detalle_ejercicio"
	template_name = "administracion/ejercicio.html"

class EjercicioVincularView(FormView):
	form_class = EjercicioVincularForm

	def form_valid(self,form):
		self.ejercicio_id = form.cleaned_data['ejercicio_id']
		return redirect('lista_ejercicios')

class EjercicioCreate(CreateView):
	model = Ejercicio
	form_class = EjercicioForm
	success_url = reverse_lazy('lista_ejercicios')
	template_name = 'administracion/nuevo_ejercicio.html'

class EjercicioUpdate(UpdateView):
	model = Ejercicio
	form_class = EjercicioForm
	success_url = reverse_lazy('lista_ejercicios')
	template_name = 'administracion/editar_ejercicio.html'

class EjercicioDelete(DeleteView):
	model = Ejercicio
	success_url = reverse_lazy('lista_ejercicios')

class JugadorListView(ListView):

	context_object_name = "lista_jugadores"
	queryset = Jugador.objects.all()
	template_name = "administracion/jugadores.html"


class JugadorDetailView(DetailView):
	model = Jugador

	def get_context_data(self, **kwargs):
		context = super(JugadorDetailView, self).get_context_data(**kwargs)
		context['resultados'] = Resultado.objects.filter(sesion__jugador=self.kwargs['pk'])
		return context

	context_object_name = "detalle_jugador"
	template_name = "administracion/jugador.html"

class JugadorCreate(FormView):
	form_class = JugadorForm
	success_url = reverse_lazy('lista_jugadores')
	template_name = 'administracion/nuevo_jugador.html'
	
	def form_valid(self, form):
		user = User(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
		user.save()
		jugador = Jugador(user=user,fecha_nacimiento=form.cleaned_data['fecha_nacimiento'])
		jugador.save()
		return super(JugadorCreate, self).form_valid(form)


class JugadorUpdate(FormView, ContextMixin):
	form_class = JugadorUpdateForm
	success_url = reverse_lazy('lista_jugadores')
	template_name = 'administracion/editar_jugador.html'

	def get_context_data(self, **kwargs):
		context = super(JugadorUpdate, self).get_context_data(**kwargs)
		context['jugador'] = Jugador.objects.get(pk=self.kwargs['pk'])
		return context

	def form_valid(self,form):
		print(form)
		jugador = Jugador.objects.get(pk=form.cleaned_data['jugador_id'])
		user = jugador.user
		user.username = form.cleaned_data['username']
		user.password = form.cleaned_data['password']
		user.save()
		jugador.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
		jugador.save()
		return super(JugadorUpdate, self).form_valid(form)

class JugadorDelete(DeleteView):
	model = Jugador
	success_url = reverse_lazy('lista_jugadores')

