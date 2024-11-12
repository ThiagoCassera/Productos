from django.shortcuts import render
from .models import Productos

# Create your views here.

def home(request):
    productos = Productos.objects.all()
    return render(request, "VistaProductos.html",{"productoslista": productos})