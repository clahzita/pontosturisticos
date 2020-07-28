from django.contrib import admin

from .actions import aprova_comentarios, reprova_comentarios
from .models import Comentario


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario','data','aprovado']
    actions = [aprova_comentarios, reprova_comentarios]


admin.site.register(Comentario, ComentarioAdmin)