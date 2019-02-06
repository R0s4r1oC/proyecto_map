from django.contrib import admin
from .models import Contrato
from .models import Unidad
from .models import Categoria
from .models import Area
from .models import Usuario
from .models import Proveedor
from .models import Ordenservicio
from .models import Ordencompra
from .models import Sedes
from .models import Tipohardware
from .models import Moviles
from .models import Hardware
from .models import Software

admin.site.register(Unidad)
admin.site.register(Categoria)
admin.site.register(Area)
admin.site.register(Usuario)
admin.site.register(Proveedor)
admin.site.register(Ordenservicio)
admin.site.register(Ordencompra)
admin.site.register(Sedes)
admin.site.register(Tipohardware)
admin.site.register(Moviles)
admin.site.register(Hardware)
admin.site.register(Software)


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_filter = ('id', 'nombre')
    search_field = ('id', 'nombre')
