from django.urls import path

from . import views





#Paths
urlpatterns = [

    #connected to the function index in  views.py
    path('login', views.login, name='login'),

    #connected to the function register 
    path('register', views.register, name='register'),

    #connected to the method logout
    path('logout', views.logout, name='logout'),

    #connected to the method dashboard single,
    path('dashboard', views.dashboard, name='dashboard'),

    #connected to the method dashboard single,
    #path('admin_listing', views.admin_listing, name='admin_listing'),
    path('admin_listings', views.AdminListView.as_view(), name='admin_listings' ),

    path('admin_listing/<int:pk>/', views.DetailListView.as_view(), name='admin_listing' ),

    path('listing_form/', views.ListingCreate.as_view(), name='listing_form' ),

    path('admin_listing/<int:pk>/', views.ListingUpdate.as_view(), name='update_form'),
    
    #path route, value to pass, function, 
    #path('delete_form/<int:pk>/', views.ListingDelete.as_view(), name='delete_form'),
]
