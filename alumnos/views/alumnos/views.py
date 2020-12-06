from django.shortcuts import render
from django.urls import reverse_lazy
from alumnos.models import alumno
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from alumnos.forms import AlumnoForm


def alumnos_list(request):
	data = {
			'alumnos': alumno.objects.all(),
			'title' : "Listado de Alumnos"
	}
	return render(request, 'alumnos/list.html', data)

class AlumnoListView(ListView):
	model = alumno
	template_name = "alumnos/list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Listado de Alumnos'
		return context

class AlumnoCreateView(CreateView):
	model = alumno
	form_class = AlumnoForm
	template_name = "alumnos/create.html"
	success_url = reverse_lazy('alumnos:lista')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Matricula de Alumno'
		return context

class AlumnoUpdateView(UpdateView):
	model= alumno
	form_class = AlumnoForm
	template_name = "alumnos/create.html"
	success_url = reverse_lazy('alumnos:lista') 

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Actualizacion de Registro de Alumno'
		return context

class AlumnoDeleteView(DeleteView):
	model = alumno
	template_name = "alumnos/delete.html"
	success_url = reverse_lazy('alumnos:lista')
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminación de Registro'
		return context