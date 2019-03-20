from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path to pages urls
    path('', include('pages.urls')),
    # path to pages urls
    path('listings/', include('listings.urls')),
    # path to pages accounts
    path('accounts/', include('accounts.urls')),
    # path to pages comtacst
    path('contacts/', include('contacts.urls')),
    # path to spyder
    #path('spyder/', include('spyder.urls')),
    # path to admin urls 
    path('admin/', admin.site.urls),
# Import media form static floder 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 