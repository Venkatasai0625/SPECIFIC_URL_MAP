from django.urls import path
from mobile.views import *
urlpatterns = [
    
    path('Oppo/',Oppo,name='Oppo'),
    path('Microsoft/',Microsoft,name='Microsoft'),
]