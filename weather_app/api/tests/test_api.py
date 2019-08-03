from django.urls import reverse
from django.test import TestCase

from core.models import History


class ApiTestCase(TestCase):
    def test_ok_weather_get(self):
        url = '{0}?city={1}'.format(reverse('weather'), 'moscow')
        response = self.client.get(url)
        self.assertTrue(response.status_code == 200)

    def test_404_weather_get(self):
        url = '{0}?city={1}'.format(reverse('weather'), 'сочи')
        response = self.client.get(url)
        self.assertTrue('404' in response.content.decode("utf-8"))

    def test_history(self):
        self.assertTrue(History.objects.all().count() == 0)
        url = '{0}?city={1}'.format(reverse('weather'), 'moscow')
        self.client.get(url)
        self.assertTrue('moscow' in History.objects.all().first().request)
