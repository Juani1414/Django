from django.contrib import admin
from .models import Servicio 

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display=("titulo", "contenido", "imagen")
    readonly_fields=('created','updated')

admin.site.register(Servicio, ServicioAdmin)
