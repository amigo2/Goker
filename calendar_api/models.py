from django.db import models
from brokers.models import Broker
from listings.models import Listing
from django.urls import reverse
from datetime import datetime

# Create your models here.


class Events(models.Model):
    
    NEWS        = 'NO'
    ADQUISITION = 'AD'
    RE_CONTACT  = 'RE'
    SALES_E     = 'CV'

    TYPE_OF_EVENT=[
        (NEWS, 'news'),
        (ADQUISITION, 'adquisition'),
        (RE_CONTACT, 're_contact'),
        (SALES_E, 'sales_e'),
    ]

    type_of_event = models.CharField(max_length=2,choices=TYPE_OF_EVENT,default=NEWS, )
    broker        = models.ForeignKey(Broker, on_delete=models.DO_NOTHING)
    listing       = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    event_name    = models.CharField(max_length=200)
    address       = models.CharField(max_length=300,blank=True)
    description   = models.TextField(blank=True)
    start_date    = models.DateTimeField(null=True,blank=True)
    end_date      = models.DateTimeField(null=True,blank=True)
    date_created  = models.DateTimeField(default=datetime.now, blank=True)
    

    def __str__(self):
        return self.event_name

        
#Pedidos
class Request(models.Model):
    name           = models.CharField(max_length=100)
    surname        = models.CharField(max_length=100)
    title          = models.CharField(max_length=200)
    address        = models.CharField(max_length=300,blank=True)
    contact        = models.CharField(max_length=100)
    description    = models.TextField(blank=True)
    caracteristics = models.TextField(blank=True)
    date_created   = models.DateTimeField(default=datetime.now, blank=True)



