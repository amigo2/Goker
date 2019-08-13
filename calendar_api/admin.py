from django.contrib import admin

# Register your models here.

from .models import Events

'''class RequestAdmin (admin.ModelAdmin):
    list_display       = ('id', 'title', 'address', 'description', 'start_date', 'end_date', 'start_time')
    list_display_links = ('id','title')
    list_filter        = ('title',)
    list_per_page      = 25'''




admin.site.register(Events)

