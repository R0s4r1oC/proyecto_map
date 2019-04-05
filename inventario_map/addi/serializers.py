from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    dni = serializers.CharField(read_only=True)
    nombres_apelldos = serializers.CharField(read_only=True)
    tipo_contrato_label = serializers.CharField(read_only=True, source='tipo_contrato.titulo')
    area_label = serializers.CharField(read_only=True, source='area.nombre')

    class Meta:
        model = Usuario
        fields = (
            'tipo_contrato',
            'area',
            'dni',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_cese',
            'email',
            'anexo',
            'nombres_apelldos',
            'tipo_contrato_label',
            'area_label'
        )
        datatables_always_serialize = ('dni', )
