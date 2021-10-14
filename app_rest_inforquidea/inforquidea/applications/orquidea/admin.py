from django.contrib import admin

from . import models
# Register your models here.
#admin.site.register(models.Orquidea)
@admin.register(models.Orquidea)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'tipo_crecimiento',
        'nombre_comun',
        'floracion',
        'duracion_flor',
        'tamaño_flor',
        'ubicacion',
    ]