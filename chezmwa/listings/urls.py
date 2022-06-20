from django.urls import path
from . import views

urlpatterns = [
    path('listing/<str:pk>/', views.listing, name='listing'),
    path('listings', views.listings, name='listings'),
    path('search/', views.search, name='search'),
]
