from django.urls import path, include, re_path

from . import views

app_name = "addi"

usuarios_urlpatterns = [
    path('', views.UsuarioListView.as_view(), name='usuario-list'),
    path('create/', views.UsuarioCreateView.as_view(), name='usuario-create'),
    re_path('(?P<pk>[0-9]{8})/update/$', views.UsuarioUpdateView.as_view(), name='usuario-update'),
    re_path('(?P<pk>[0-9]{8})/delete/$', views.UsuarioDeleteView.as_view(), name='usuario-delete'),
    path('delete/', views.UsuariosDeleteView.as_view(), name='usuarios-delete'),
    path('api-list/', views.UsuarioAPIList.as_view(), name='usuario-api-list'),
    re_path('api-list/(?P<pk>[0-9]{8})/$', views.UsuarioAPIRetrieve.as_view(), name='usuario-api-detail'),
]

urlpatterns = [
    path('usuarios/', include(usuarios_urlpatterns)),
]
