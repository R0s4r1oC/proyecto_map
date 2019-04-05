from django.contrib import admin

from .models import (
    Contrato, Unidad, Categoria, Area, Usuario, Proveedor, OrdenServicio,
    OrdenCompra, Sedes, TipoHardware, Moviles, Hardware, Software
)

admin.site.register(Unidad)
admin.site.register(Categoria)
admin.site.register(Area)
admin.site.register(Usuario)
admin.site.register(Proveedor)
admin.site.register(OrdenServicio)
admin.site.register(OrdenCompra)
admin.site.register(Sedes)
admin.site.register(TipoHardware)
admin.site.register(Moviles)
admin.site.register(Hardware)
admin.site.register(Software)


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    list_filter = ('titulo', )
    search_field = ('titulo', )
