from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Carretera, Tramo, CategoriaCarretera


def index(request):
    return render(request, 'carreteras/index.html')

def lista_carreteras(request):
    carreteras = Carretera.objects.all()
    return render(request, 'carreteras/carretera_list.html', {'carreteras': carreteras})

def detalle_carretera(request, pk):
    carretera = get_object_or_404(Carretera, pk=pk)
    return render(request, 'carreteras/carretera_detail.html', {'carretera': carretera})

def crear_carretera(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria_id = request.POST['categoria']
        nueva_categoria = request.POST.get('nueva_categoria', '').strip()  # Campo para nueva categoría

        if nueva_categoria:
            categoria, created = CategoriaCarretera.objects.get_or_create(nombre=nueva_categoria)
            categoria_id = categoria.id  # Usamos la nueva categori creada o la existente

        Carretera.objects.create(nombre=nombre, categoria_id=categoria_id)
        return HttpResponseRedirect(reverse('carreteras'))  # Redirige a la lista de carreteras

    categorias = CategoriaCarretera.objects.all()  # Obtenemos todas las categorias existentes
    return render(request, 'carreteras/carretera_form.html', {'categorias': categorias})

def editar_carretera(request, pk):
    carretera = get_object_or_404(Carretera, pk=pk)
    if request.method == 'POST':
        carretera.nombre = request.POST['nombre']
        categoria_id = request.POST['categoria']
        nueva_categoria = request.POST.get('nueva_categoria', '').strip()

        if nueva_categoria:
            categoria, created = CategoriaCarretera.objects.get_or_create(nombre=nueva_categoria)
            categoria_id = categoria.id  # Usamos la nueva categoría recién creada o existente

        carretera.nombre = request.POST['nombre']
        carretera.categoria_id = categoria_id
        carretera.save()
        return HttpResponseRedirect(reverse('carreteras'))  # Redirige a la lista de carreteras

    categorias = CategoriaCarretera.objects.all()  # Obtener todas las categorías existentes
    return render(request, 'carreteras/carretera_form.html', {'carretera': carretera, 'categorias': categorias})


def eliminar_carretera(request, pk):
    carretera = get_object_or_404(Carretera, pk=pk)
    if request.method == 'POST':
        carretera.delete()
        return HttpResponseRedirect(reverse('carreteras'))
    return render(request, 'carreteras/carretera_confirm_delete.html', {'carretera': carretera})

def lista_tramos(request, carretera_id):
    carretera = get_object_or_404(Carretera, id=carretera_id)
    tramos = Tramo.objects.filter(carretera=carretera)
    return render(request, 'carreteras/tramo_list.html', {'tramos': tramos, 'carretera': carretera})

def detalle_tramo(request, tramo_id):
    tramo = get_object_or_404(Tramo, id=tramo_id)
    return render(request, 'carreteras/tramo_detail.html', {'tramo': tramo})

def crear_tramo(request, carretera_id):
    carretera = get_object_or_404(Carretera, id=carretera_id)
    if request.method == 'POST':
        comuna_inicio = request.POST['comuna_inicio']
        comuna_termino = request.POST['comuna_termino']
        km_inicio = request.POST['km_inicio']
        km_termino = request.POST['km_termino']
        Tramo.objects.create(carretera=carretera, comuna_inicio=comuna_inicio, comuna_termino=comuna_termino, km_inicio=km_inicio, km_termino=km_termino)
        return HttpResponseRedirect(reverse('lista_tramos', args=[carretera.id]))
    return render(request, 'carreteras/tramo_form.html', {'carretera': carretera})

def editar_tramo(request, tramo_id):
    tramo = get_object_or_404(Tramo, id=tramo_id)
    if request.method == 'POST':
        tramo.comuna_inicio = request.POST['comuna_inicio']
        tramo.comuna_termino = request.POST['comuna_termino']
        tramo.km_inicio = request.POST['km_inicio']
        tramo.km_termino = request.POST['km_termino']
        tramo.save()
        return HttpResponseRedirect(reverse('detalle_tramo', args=[tramo.id]))
    return render(request, 'carreteras/tramo_form.html', {'tramo': tramo})

def eliminar_tramo(request, tramo_id):
    tramo = get_object_or_404(Tramo, id=tramo_id)
    if request.method == 'POST':
        tramo.delete()
        return HttpResponseRedirect(reverse('lista_tramos', args=[tramo.carretera.id]))
    return render(request, 'carreteras/tramo_confirm_delete.html', {'tramo': tramo})

