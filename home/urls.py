from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home.home'),
    path('get_data/', views.get_data, name="home.get_data")
]
