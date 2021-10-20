from django.contrib import admin

from . import models
# Register your models here.
#admin.site.register(models.Orquidea)
@admin.register(models.Vivero)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombrempresa',
        'propietario',
        'cantorq',
        'contacto',
        'ubicacion',
    ]