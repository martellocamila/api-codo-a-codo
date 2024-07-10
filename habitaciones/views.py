from django.shortcuts import render, redirect
from .models import Habitacion
import os
import uuid
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json

def inicio(request):
    habitaciones = Habitacion.objects.all()
    data = {
        'habitaciones': habitaciones,
    }
    return render(request, 'habitaciones/home.html', data)

def alta_habitacion(request):
    return render(request, 'habitaciones/alta_habitacion.html')

def store(request):
    if request.method == 'POST':
        nombre_hab = request.POST.get('txtNombre')
        descripcion_hab = request.POST.get('txtDescripcion')
        precio_hab = request.POST.get('txtPrecio')
        foto_hab = request.FILES.get('txtFoto')

        if foto_hab:
            foto_hab = generate_unique_filename(foto_hab)

        # Procesa los datos y guarda en la base de datos
        habitacion = Habitacion(
            nombre=nombre_hab,
            descripcion=descripcion_hab,
            precio=precio_hab,
            foto=foto_hab
        )
        habitacion.save()

    return redirect('/')

def delete(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, pk=habitacion_id)

    # Guarda la ruta de la foto antes de eliminar la habitación
    foto_path = habitacion.foto.path if habitacion.foto else None

    # Elimina la habitación de la base de datos
    habitacion.delete()

    # Elimina la foto asociada si existe
    if foto_path and os.path.exists(foto_path):
        os.remove(foto_path)

    return redirect('/')


# Genera un nombre único para el archivo utilizando UUID y conserva la extensión.
def generate_unique_filename(file):
    extension = os.path.splitext(file.name)[1]
    unique_name = f'{uuid.uuid4()}{extension}'
    return SimpleUploadedFile(unique_name, file.read())






    