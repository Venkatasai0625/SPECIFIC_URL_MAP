from django.urls import path
from shopping.views import *
urlpatterns = [
    
    path('Jeans/',Jeans,name='Jeans'),
    path('Shirts/',Shirts,name='Shirts'),
]