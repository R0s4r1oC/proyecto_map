from django import forms
from django.urls import reverse_lazy
from django.conf import settings

from crispy_forms.helper import FormHelper

from .models import Usuario


class UsuarioForm(forms.ModelForm):

    fecha_cese = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'placeholder': 'dd/mm/yyyy'
            }
        ),
        input_formats=settings.DATE_INPUT_FORMATS
    )

    class Meta:
        model = Usuario
        fields = (
            'dni', 'nombre', 'apellido_paterno', 'apellido_materno',
            'fecha_cese', 'email', 'anexo', 'tipo_contrato', 'area',
        )

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-9'
        self.helper.form_id = 'id-usuarioForm'
        self.helper.form_action = reverse_lazy('addi:usuario-create')
