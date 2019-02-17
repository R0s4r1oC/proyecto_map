from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from http import HTTPStatus

from rest_framework import generics

from .models import Usuario
from .forms import UsuarioForm
from .serializers import UsuarioSerializer


class UsuarioListView(TemplateView):

    model = Usuario
    template_name = 'addi/usuario_list.html'

    def get_queryset(self):
        queryset = self.model.objects.select_related(
            'tipo_contrato', 'area'
        ).all()
        return queryset

    def get_context_data(self, **kwargs):
        extra_content = dict(
            app_title='Módulo de Usuarios - PNSU',
        )
        context = super().get_context_data(**kwargs)
        context.update(extra_content)
        return context


class UsuarioAPIList(generics.ListAPIView):
    queryset = Usuario.objects.select_related(
        'tipo_contrato', 'area'
    ).all()
    serializer_class = UsuarioSerializer


class UsuarioAPIRetrieve(generics.RetrieveAPIView):
    queryset = Usuario.objects.select_related(
        'tipo_contrato', 'area'
    ).all()
    serializer_class = UsuarioSerializer


class UsuarioCreateView(CreateView):

    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('addi:usuario-create')
    template_name = 'addi/modal/usuario/ajax_usuario_form.html'

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form),
            status=HTTPStatus.BAD_REQUEST
        )


class UsuarioUpdateView(UpdateView):

    model = Usuario
    form_class = UsuarioForm
    template_name = 'addi/modal/usuario/ajax_usuario_form.html'

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form),
            status=HTTPStatus.BAD_REQUEST
        )

    def get_success_url(self):
        return reverse('addi:usuario-api-detail', args=(self.object.pk, ))


class UsuarioDeleteView(DeleteView):

    model = Usuario
    success_url = reverse_lazy('addi:usuario-api-list')
    template_name = 'addi/modal/usuario/ajax_usuario_delete.html'


class UsuariosDeleteView(View):

    model = Usuario
    success_url = reverse_lazy('addi:usuario-api-list')
    template_name = 'addi/modal/usuario/ajax_usuario_delete.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        pks = self.request.GET.getlist('pks')
        if pks:
            context['object_list'] = self.model.objects.filter(pk__in=pks)
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        pks = self.request.POST.getlist('pks')
        self.model.objects.filter(pk__in=pks).delete()
        return redirect(self.success_url)
