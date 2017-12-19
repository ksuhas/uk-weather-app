from rest_framework import serializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from app.models import *


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ('region', 'Ttype', 'data','year','month')


class minWeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ('data','month')


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

