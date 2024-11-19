from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Productos

# Create your views here.

def home(request):
    productos = Productos.objects.all()
    return render(request, "VistaProductos.html",{"productoslista": productos})

def FormularioProductos(request):
    return render(request, 'FormularioProductos.html')
def pruebaformulario(request):
   return render(request, 'pruebaformulario.html')

def registrarProducto(request):
    if request.method == 'POST':
        fecha_ingreso = request.POST.get('fecha')
        nombre_producto = request.POST.get('producto')
        categoria = request.POST.get('categoria')
        stock_min = request.POST.get('stock_min')
        stock_max = request.POST.get('stock_max')
        codigo_producto = request.POST.get('codigo')
        unidad = request.POST.get('unidad')
        cant_stock = request.POST.get('cantidad_stock')
        estado = request.POST.get('estado')
        observaciones = request.POST.get('observaciones')

        # Validar campos obligatorios
        if not nombre_producto:
            return HttpResponse("El campo 'producto' es obligatorio.", status=400)

        # Guardar el producto
        Productos.objects.create(
            fecha_ingreso=fecha_ingreso,
            nombre_producto=nombre_producto,
            categoria=categoria,
            stock_min=stock_min,
            stock_max=stock_max,
            codigo_producto=codigo_producto,
            unidad=unidad,
            cant_stock=cant_stock,
            Estado=estado,
            observaciones=observaciones,
        )
        return redirect('/')
    return HttpResponse("Método no permitido", status=405)

def edicionProducto(request, codigo_producto):
    producto = get_object_or_404(Productos, codigo_producto = codigo_producto)
    return render(request, 'pruebaformulario.html', {"producto": producto})

def editarProducto(request):
    fecha_ingreso = request.POST.get('fecha')
    nombre_producto = request.POST.get('producto')
    categoria = request.POST.get('categoria')
    stock_min = request.POST.get('stock_min')
    stock_max = request.POST.get('stock_max')
    codigo_producto = request.POST.get('codigo')
    unidad = request.POST.get('unidad')
    cant_stock = request.POST.get('cantidad_stock')
    estado = request.POST.get('estado')
    observaciones = request.POST.get('observaciones')

    producto = Productos.objects.get(codigo_producto = codigo_producto)
    producto.fecha_ingreso=fecha_ingreso
    producto.nombre_producto=nombre_producto
    producto.categoria=categoria
    producto.stock_min=stock_min
    producto.stock_max=stock_max
    producto.codigo_producto=codigo_producto
    producto.unidad=unidad
    producto.cant_stock=cant_stock
    producto.Estado=estado
    producto.observaciones=observaciones
    producto.save()
    return redirect('/')
    

def eliminacionProducto(request, codigo_producto):
    producto = get_object_or_404(Productos, codigo_producto = codigo_producto)
    producto.delete()
    return redirect('/')