from django.db import models


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
    tipo_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    dni = models.CharField(primary_key=True, max_length=8, db_index=True)
    nombre = models.CharField(max_length=50)
    fecha_cese = models.DateTimeField(auto_now=True)
    email = models.CharField(max_length=100)
    anexo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    ruc = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField(blank=True)
    telefono = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return self.nombre


class OrdenServicio(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    fecha_adquisicion = models.DateTimeField(auto_now=True)
    provedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=200)
    cod_pedido = models.IntegerField()
    unidad_medida = models.CharField(max_length=50)
    valor_total = models.IntegerField()

    def __str__(self):
        return self.provedor


class OrdenCompra(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    fecha_compra = models.DateTimeField(auto_now=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=100)
    cod_pedido = models.IntegerField()
    unidad_medida = models.CharField(max_length=50)
    valor_total = models.IntegerField()

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


class TipoHardware(models.Model):
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

    def __str__(self):
        return self.usuario


class Hardware(models.Model):
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


class Software(models.Model):
    serial = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Ordencompra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.cod_patrimonio
