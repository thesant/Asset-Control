from django.test import Client, TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):

    def test_views_home(self):
        self.Client = Client()
        response = self.client.get(reverse('inventory:home'))
        self.assertEqual(response.status_code, 302)
