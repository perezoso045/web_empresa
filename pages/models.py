from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
	title = models.CharField(verbose_name="Titulo", max_length=200)
	content = RichTextField(verbose_name="Contenido")
	order = models.SmallIntegerField(verbose_name="Orden", default=0)
	created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
	update  = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")
	
	#configuracion al español de la ventana admin
	class Meta:
		verbose_name = "Pagina"
		verbose_name_plural = "Paginas"
		ordering = ["order","title"]
		
	def __str__(self): #para agregar el nombre del proyecto
		return self.title
