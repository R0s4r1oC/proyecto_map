from django.db import models

from model_utils.models import TimeStampedModel


class Contrato(TimeStampedModel):
    titulo = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo


class Unidad(TimeStampedModel):
    unidad = models.CharField(max_length=50)

    def __str__(self):
        return self.unidad


class Categoria(TimeStampedModel):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Area(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Usuario(TimeStampedModel):
    tipo_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    dni = models.CharField(
        verbose_name='D.N.I',
        primary_key=True,
        max_length=8,
        db_index=True,
    )
    nombre = models.CharField(max_length=150)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    fecha_cese = models.DateField(blank=True, null=True)
    email = models.EmailField()
    anexo = models.CharField(max_length=50)

    class Meta:
        ordering = ('nombre', 'apellido_paterno', 'apellido_materno')

    def __str__(self):
        return self.nombres_apelldos

    @property
    def nombres_apelldos(self):
        return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'


class Proveedor(TimeStampedModel):
    ruc = models.IntegerField(primary_key=True)
    razon_social = models.CharField('Razón Social', max_length=150)
    direccion = models.TextField('Dirección', blank=True)
    telefono = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return self.nombre


class OrdenServicio(TimeStampedModel):
    provedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10, db_index=True)
    fecha_adquisicion = models.DateField()
    concepto = models.TextField()
    cod_pedido = models.CharField(max_length=10, db_index=True)
    unidad_medida = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.provedor


class OrdenCompra(TimeStampedModel):
    id_orden = models.IntegerField(primary_key=True)
    fecha_compra = models.DateTimeField(auto_now=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=100)
    cod_pedido = models.IntegerField()
    unidad_medida = models.CharField(max_length=50)
    valor_total = models.IntegerField()

    def __str__(self):
        return self.proveedor


class Sedes(TimeStampedModel):
    direccion = models.CharField(max_length=100)
    denominacion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    encargado = models.ForeignKey(Usuario, on_delete=True)
    anexo = models.IntegerField()

    def __str__(self):
        return self.denominacion


class TipoHardware(TimeStampedModel):
    tipo_hardware = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_hardware


class Moviles(TimeStampedModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    imei = models.CharField(max_length=16)
    fecha_asignacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario


class Hardware(TimeStampedModel):
    cod_patrimonio = models.IntegerField()
    tipo_hardware = models.ForeignKey(TipoHardware, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    fecha_garantia = models.DateTimeField(auto_now=True)
    serie = models.CharField(max_length=100)
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)

    def __str__(self):
        return self.cod_patrimonio


class Software(TimeStampedModel):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Ordencompra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    serial = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.cod_patrimonio
