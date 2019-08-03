from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from core.helper import get_weather, WeatherAPIException, request_log
from core.models import History
from api.serializer import HistorySerializer


class WeatherView(APIView):
    @staticmethod
    def get(request, format=None):
        city = request.GET.get('city')
        try:
            data = get_weather(city)
        except (WeatherAPIException, KeyError) as e:
            data = e.message
        finally:
            request_log(request, data)
            return Response(data)


class HistoryList(generics.ListCreateAPIView):
    http_method_names = ['get']
    queryset = History.objects.all()
    serializer_class = HistorySerializer
