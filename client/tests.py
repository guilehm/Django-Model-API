from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
# Create your tests here.


class HomeViewTest(TestCase):

    def test_index_status_code(self):
        client = Client()
        response = client.get(reverse('client:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_template_used(self):
        client = Client()
        response = client.get(reverse('client:index'))
        self.assertTemplateUsed(response, 'client/index.html')
        self.assertTemplateUsed(response, 'client/base.html')

    def test_products_template_used(self):
        client = Client()
        response = client.get(reverse('client:products'))
        self.assertTemplateUsed(response, 'client/products.html')
        self.assertTemplateUsed(response, 'client/base.html')