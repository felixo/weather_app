import json
import requests
import time

from django.conf import settings

from core.models import History


class WeatherAPIException(Exception):
    def __init__(self, message):
        self.message = message


def get_weather(city):
    """
    Get weather by city. For more information https://openweathermap.org/api
    :param city: city name - unicode
    :type city: basestring
    :return: dict(name, temp)
    :rtype: dict
    """
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={token}'
    url = base_url.format(city=city, token=settings.WEATHER_API_KEY)
    attempt = 0
    while attempt < settings.WEATHER_API_ATTEMPTS:
        try:
            data = requests.get(url)
            if data.status_code == 200:
                return dict(name=data.json().get('name'), temp=data.json()['main']['temp']-273)
            elif data.status_code == 404:
                raise WeatherAPIException('404 City Not Found')
            else:
                raise WeatherAPIException('Fail to get data from weather api')
        except (WeatherAPIException, KeyError) as e:
            raise e
        attempt += 1
        time.sleep(settings.WEATHER_API_TIMEOUT)


def request_log(request, data):
    History.objects.create(
        user=None if request.user.is_anonymous else request.user,
        request=request.get_full_path(),
        response=json.dumps(data) if isinstance(data, dict) else data
    )
