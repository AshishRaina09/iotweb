from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, Http404

from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics, permissions, status
from rest_framework.parsers import JSONParser
from .models import LED_bulb, Exhaus_Fan
from rest_framework.decorators import api_view


# for LED Buld only
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import LED_bulbSerializer, Exhaus_FanSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


class LED_bulbList(APIView):
    def get(self, request, format = None):
        led_bulb = LED_bulb.objects.all()
        serializer = LED_bulbSerializer(led_bulb, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):
        
        # data = JSONParser().parse(request)
        
        
        # print('date ',led_bulb)
        serializer = LED_bulbSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
class Exhaus_FanList(APIView):
    def get(self, request, format = None):
        exhaus_fan = Exhaus_Fan.objects.all()
        serializer = Exhaus_FanSerializer(exhaus_fan, many = True)
        return Response(serializer.data)

class LED_bulb_pd(APIView):
    
    def get_object(self, id):
        try:
            return LED_bulb.objects.get(id = id)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, format = None):
        id = request.data.get('id')
        led_bulb = self.get_object(id)
        serializer = LED_bulbSerializer(led_bulb)
        return Response(serializer.data)

    def put(self, request, format = None):
        # print("Type is ", type(id), id, request.data.get('id') )
        id = request.data.get('id')
        led_bulb =self.get_object( id )
        serializer = LED_bulbSerializer(led_bulb, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, format = None):
        id = request.data.get('id')
        led_bulb = self.get_object(id)
        led_bulb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

