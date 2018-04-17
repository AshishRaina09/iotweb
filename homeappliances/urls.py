from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LED_bulbList, Exhaus_FanList
from homeappliances import views


app_name = 'homeappliances'

urlpatterns = [
    path('ledbulb',  LED_bulbList.as_view(), name = 'ledbulb'),
	path('exhaust_fan',  LED_bulbList.as_view(), name = 'ledbulb'),
    

]
urlpatterns = format_suffix_patterns(urlpatterns)           