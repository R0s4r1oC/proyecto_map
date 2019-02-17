from http import HTTPStatus

from django.test import TestCase, Client
from django.urls import reverse


class UsuarioTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_usuarios(self):
        url = reverse('addi:usuario-list')
        list_response = self.client.get(url)

        url = reverse('addi:usuario-create')
        create_response = self.client.get(url)

        self.assertEqual(list_response.status_code, HTTPStatus.OK)
        self.assertEqual(create_response.status_code, HTTPStatus.OK)
