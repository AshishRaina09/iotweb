from django.db import models





class LED_bulb(models.Model):
    state = models.BooleanField(default = False,null=False,blank=False)
    
    def __str__(self):
       return 'state'

class Exhaus_Fan(models.Model):
    state = models.BooleanField(default = False,null=False,blank=False)
    
    def __str__(self):
       return 'state'

