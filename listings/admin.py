from django.contrib import admin

from .models import Listing



class ListingAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'reference', 'is_published', 'price', 'list_date', 'broker')
    list_display_links = ('id','title')
    list_filter = ('broker',)
    list_editable = ('is_published',)
    search_fields = ('title', 'reference', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

