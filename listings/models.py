from django.db import models
from django.urls import reverse
from datetime import datetime
from brokers.models import Broker


class Listing(models.Model):
    broker       = models.ForeignKey(Broker, on_delete=models.DO_NOTHING)
    reference    = models.CharField(max_length=20, blank=True)
    title        = models.CharField(max_length=200)
    address      = models.CharField(max_length=200,blank=True)
    city         = models.CharField(max_length=100,blank=True)
    state        = models.CharField(max_length=100,blank=True)
    zipcode      = models.CharField(max_length=20,blank=True)
    description  = models.TextField(blank=True)
    price        = models.IntegerField()
    bedrooms     = models.IntegerField(blank=True)
    bathrooms    = models.IntegerField(blank=True)
    garage       = models.IntegerField(blank=True)
    mtrs         = models.IntegerField(blank=True)
    lot_size     = models.IntegerField(blank=True)
    photo_main   = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1      = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_2      = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3      = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4      = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5      = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6      = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True)
    list_date    = models.DateTimeField(default=datetime.now, blank=True)

    # This is redirecting the model to admin_listing.html, but is returning from submit new property a wrong url.
    def get_absolute_url(self):
        return reverse('admin_listing', kwargs={ 'pk': self.pk})

    def __str__(self):
        return self.title