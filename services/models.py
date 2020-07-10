from django.db import models

# Create your models here.
class Service(models.Model):
	title = models.CharField(max_length=200, verbose_name = "Titulo" )
	subtitle = models.CharField(max_length=200, verbose_name = "Subtitulo" )
	content =models.TextField(verbose_name = "Contenido")
	image = models.ImageField(verbose_name = "Imagen", upload_to = "services")
	created = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha de creación")
	update  = models.DateTimeField(auto_now = True, verbose_name = "Fecha de edición")
	
    
	#configuracion al español de la ventana admin
	class Meta:
		verbose_name = "servicio"
		verbose_name_plural = "servicios"
		ordering = ["-created"]
		
	def __str__(self): #para agregar el nombre del proyecto
		return self.title 
