from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/<str:pk>/', views.listing, name='listing'),
    path('listings', views.listings, name='listings'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
]
