from django.db import models

# Create your models here.
class alumno(models.Model):
	nombres = models.CharField(max_length=150, verbose_name="Nombres")
	apellidos = models.CharField(max_length=150, verbose_name="Apellidos")
	genero = models.CharField(max_length=1, verbose_name="Genero", default="M")
	edad =models.PositiveIntegerField(default=0)
	avatar=models.ImageField(upload_to="avatar", null=True, blank=True)
	adjuntos = models.FileField(upload_to="files", null=True, blank=True)

	def __str__(self):
		return self.nombres

	class Meta:
		verbose_name = "Alumno"
		verbose_name_plural = "Alumnos"
		db_table = "Alumnos"
		ordering = ['id']
