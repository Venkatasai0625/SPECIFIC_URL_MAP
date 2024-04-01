from django.shortcuts import render

# Create your views here.
def Shirts(request):
    return render(request,'shirts.html')
def Jeans(request):
    return render(request,'jeans.html')