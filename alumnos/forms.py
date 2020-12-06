from django.forms import ModelForm
from alumnos.models import alumno

class AlumnoForm(ModelForm):
	class Meta:
		model = alumno
		fields = '__all__'