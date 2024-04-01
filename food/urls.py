from django.urls import path
from food.views import *
urlpatterns = [
    
    path('Biryani/',Biryani,name='Biryani'),
    path('prawns/',prawns,name='prawns'),
]