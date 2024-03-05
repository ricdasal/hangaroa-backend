from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

def lista_blog(request):
    blogs = Blog.objects.all()
    data = {'blogs': list(blogs.values())}
    return JsonResponse(data)

@csrf_exempt
def crear_blog(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        nuevo_blog = Blog.objects.create(
            titulo=datos['titulo'],
            texto=datos['texto'],
            fecha=datos['fecha'],
            imagen=datos['imagen'],
            estado=datos['estado']
        )
        return JsonResponse({'mensaje': 'Registro de Blog creado exitosamente'})
    else:
        return JsonResponse({'error': 'Esta vista solo permite solicitudes POST'})


@csrf_exempt
def editar_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return JsonResponse({'error': 'El blog especificado no existe'}, status=404)

    if request.method == 'PUT':
        datos = json.loads(request.body)
        try:
            blog.titulo = datos['titulo']
            blog.texto = datos['texto']
            blog.fecha = datos['fecha']
            blog.imagen = datos['imagen']
            blog.estado = datos['estado']
            blog.save()
            return JsonResponse({'mensaje': 'Blog editado exitosamente'})
        except KeyError:
            return JsonResponse({'error': 'Datos incompletos o incorrectos'})
    else:
        return JsonResponse({'error': 'Esta vista solo permite solicitudes PUT'})

@csrf_exempt 
def eliminar_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return JsonResponse({'error': 'El blog especificado no existe'}, status=404)

    if request.method == 'DELETE':
        blog.estado = False
        return JsonResponse({'mensaje': 'Blog eliminado exitosamente'})
    else:
        return JsonResponse({'error': 'Esta vista solo permite solicitudes DELETE'})
