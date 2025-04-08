from django.urls import path 
from . import views   

urlpatterns = [
    path('', views.home, name='blog-home'),  # URL pattern for the home view
    path('about/', views.about, name='blog-about'),  # URL pattern for the about view
]