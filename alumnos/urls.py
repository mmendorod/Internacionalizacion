from django.urls import path
from alumnos.views.alumnos.views import *

app_name="alumnos"

urlpatterns =[ 
	path('list/', AlumnoListView.as_view(), name="lista"),
	path('add/' ,AlumnoCreateView.as_view(), name="crear"),
	path('edit/<int:pk>/', AlumnoUpdateView.as_view() , name="editar"),
	path('delete/<int:pk>/', AlumnoDeleteView.as_view() , name="eliminar"),



]