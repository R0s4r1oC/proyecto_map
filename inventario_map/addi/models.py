# Create your models here.
from django.db import models
from django.utils import timezone


class Contrato(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Unidad(models.Model):
    unidad = models.CharField(max_length=50)

    def __str__(self):
        return self.unidad


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Area(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    dni_id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    tipo_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    fecha_cese = models.DateTimeField(auto_now=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    anexo = models.CharField(max_length=50)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    ruc = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre


class Ordenservicio(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    fecha_adquisicion = models.DateTimeField(auto_now=True)
    provedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=200)
    cod_pedido = models.IntegerField()
    Unidad_medida = models.CharField(max_length=50)
    valor_total = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.provedor


class Ordencompra(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    fecha_compra = models.DateTimeField(auto_now=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=100)
    cod_pedido = models.IntegerField()
    Unidad_medida = models.CharField(max_length=50)
    valor_total = models.IntegerField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.proveedor


class Sedes(models.Model):
    direccion = models.CharField(max_length=100)
    denominacion = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    encargado = models.ForeignKey(Usuario, on_delete=True)
    anexo = models.IntegerField()

    def __str__(self):
        return self.denominacion


class Tipohardware(models.Model):
    tipo_hardware = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_hardware


class Moviles(models.Model):
    numero = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    imei = models.CharField(max_length=16)
    fecha_asignacion = models.DateTimeField(auto_now=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.usuario


class Hardware(models.Model):
    cod_patrimonio = models.IntegerField()
    tipo_hardware = models.ForeignKey(Tipohardware, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    fecha_garantia = models.DateTimeField(auto_now=True)
    serie = models.CharField(max_length=100)
    orden_compra = models.ForeignKey(Ordencompra, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sedes,on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.cod_patrimonio

