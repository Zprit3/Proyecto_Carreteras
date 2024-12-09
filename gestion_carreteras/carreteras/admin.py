from django.contrib import admin
from .models import CategoriaCarretera, Carretera, Comuna, Tramo


class CategoriaCarreteraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


class CarreteraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria')
    search_fields = ('nombre',)
    list_filter = ('categoria',)


class ComunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


class TramoAdmin(admin.ModelAdmin):
    list_display = ('id', 'carretera', 'km_inicio', 'km_termino', 'comuna_inicio', 'comuna_termino', 'es_inicio_carretera', 'es_fin_carretera', 'confluye_con')
    search_fields = ('carretera__nombre', 'comuna_inicio__nombre', 'comuna_termino__nombre')
    list_filter = ('carretera', 'es_inicio_carretera', 'es_fin_carretera')
    autocomplete_fields = ('carretera', 'comuna_inicio', 'comuna_termino', 'confluye_con', 'comuna_confluencia')
    actions = ['marcar_como_inicio', 'marcar_como_fin']

    def marcar_como_inicio(self, request, queryset):
        queryset.update(es_inicio_carretera=True)
        self.message_user(request, "Los tramos seleccionados ahora son inicio de carretera.")

    def marcar_como_fin(self, request, queryset):
        queryset.update(es_fin_carretera=True)
        self.message_user(request, "Los tramos seleccionados ahora son fin de carretera.")

    marcar_como_inicio.short_description = "Marcar como inicio de carretera"
    marcar_como_fin.short_description = "Marcar como fin de carretera"


admin.site.register(CategoriaCarretera, CategoriaCarreteraAdmin)
admin.site.register(Carretera, CarreteraAdmin)
admin.site.register(Comuna, ComunaAdmin)
admin.site.register(Tramo, TramoAdmin)
