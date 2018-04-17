from rest_framework import serializers
from .models import LED_bulb, Exhaus_Fan

# LED Serializer For Api

class LED_bulbSerializer(serializers.ModelSerializer):
    class Meta:
        model = LED_bulb
        fields = '__all__'    
        verbose_name = 'LED'
        verbose_name_plural = 'LEDs'
		
class Exhaus_FanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LED_bulb
        fields = '__all__'    
        verbose_name = 'LED'
        verbose_name_plural = 'LEDs'


