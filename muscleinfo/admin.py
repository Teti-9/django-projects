from django.contrib import admin
from .models import Exercicio

@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):

    list_display = ('nome', 'musculo', 'musculo_residual', 'series', 'carga', 'repeticoes', 'infos')

    exclude = ('carga_anterior', 'repeticoes_anterior', 'data', 'data_anterior', 'user_id')
    
    search_fields = ('nome', 'musculo')

    list_filter = ('musculo',)