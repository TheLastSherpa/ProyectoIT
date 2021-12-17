from django.shortcuts import render
from django.http import HttpResponse
from AppInvIT.models import *
from AppInvIT.forms import *

# Home de la web
def inicio(request):
    return render(request, 'AppInvIT/inicio.html')

# Notebooks
def notebooks(request):
    return render(request, 'AppInvIT/notebooks.html')

# Desktops
def desktops(request):
    return render(request, 'AppInvIT/desktops.html')

# Servers
def servers(request):
    return render(request, 'AppInvIT/servers.html')

# Storages
def storages(request):
    return render(request, 'AppInvIT/storages.html')

# Agregar una nueva Notebook:
def notebookFormulario(request):
    if request.method == 'POST':
        miFormulario = NotebookFormulario(request.POST)
        if miFormulario.is_valid():
            dato = miFormulario.cleaned_data
            notebook = Notebook(
                marca=dato['marca'],
                modelo=dato['modelo'],
                numeroSerie=dato['numeroSerie']
                )
            notebook.save()
            return render(request, 'AppInvIT/notebooks.html')
    else:
        miFormulario = NotebookFormulario()
    return render(request, 'AppInvIT/notebooksFormulario.html', {'miFormulario':miFormulario})

# Agregar una nueva Desktop:
def desktopFormulario(request):
    if request.method == 'POST':
        miFormulario = DesktopFormulario(request.POST)
        if miFormulario.is_valid():
            dato = miFormulario.cleaned_data
            desktop = Desktop(
                marca=dato['marca'],
                modelo=dato['modelo'],
                numeroSerie=dato['numeroSerie']
                )
            desktop.save()
            return render(request, 'AppInvIT/desktops.html')
    else:
        miFormulario = DesktopFormulario()
    return render(request, 'AppInvIT/desktopsFormulario.html', {'miFormulario':miFormulario})

# Agregar un nuevo Server:
def serverFormulario(request):
    if request.method == 'POST':
        miFormulario = ServerFormulario(request.POST)
        if miFormulario.is_valid():
            dato = miFormulario.cleaned_data
            server = Server(
                marca=dato['marca'],
                modelo=dato['modelo'],
                numeroSerie=dato['numeroSerie'],
                esRackeable=dato['esRackeable']
                )
            server.save()
            return render(request, 'AppInvIT/servers.html')
    else:
        miFormulario = ServerFormulario()
    return render(request, 'AppInvIT/serversFormulario.html', {'miFormulario':miFormulario})

# Agregar un nuevo Storage:
def storageFormulario(request):
    if request.method == 'POST':
        miFormulario = StorageFormulario(request.POST)
        if miFormulario.is_valid():
            dato = miFormulario.cleaned_data
            storage = Storage(
                marca=dato['marca'],
                modelo=dato['modelo'],
                numeroSerie=dato['numeroSerie'],
                almacenamiento=dato['almacenamiento'],
                esRackeable=dato['esRackeable']
                )
            storage.save()
            return render(request, 'AppInvIT/storages.html')
    else:
        miFormulario = StorageFormulario()
    return render(request, 'AppInvIT/storagesFormulario.html', {'miFormulario':miFormulario})

# Busqueda Notebook
def busquedaNotebook(request):
    return render(request, 'AppInvIT/busquedaNotebook.html')

def buscarNotebook(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        notebooks = Notebook.objects.filter(marca__icontains=marca)
        
        return render(request, "AppInvIT/resultadoBusquedaNotebook.html",{"notebooks":notebooks, "marca":marca})
    else:
        respuesta = "Che, mandame información!"
    return HttpResponse(respuesta)

# Busqueda Desktop
def busquedaDesktop(request):
    return render(request, 'AppInvIT/busquedaDesktop.html')

def buscarDesktop(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        desktops = Desktop.objects.filter(marca__icontains=marca)
        
        return render(request, "AppInvIT/resultadoBusquedaDesktop.html",{"desktops":desktops, "marca":marca})
    else:
        respuesta = "Che, mandame información!"
    return HttpResponse(respuesta)

# Busqueda Server
def busquedaServer(request):
    return render(request, 'AppInvIT/busquedaServer.html')

def buscarServer(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        servers = Server.objects.filter(marca__icontains=marca)
        
        return render(request, "AppInvIT/resultadoBusquedaServer.html",{"servers":servers, "marca":marca})
    else:
        respuesta = "Che, mandame información!"
    return HttpResponse(respuesta)

# Busqueda Storage
def busquedaStorage(request):
    return render(request, 'AppInvIT/busquedaStorage.html')

def buscarStorage(request):
    if request.GET["marca"]:
        marca = request.GET["marca"]
        storages = Storage.objects.filter(marca__icontains=marca)
        
        return render(request, "AppInvIT/resultadoBusquedaStorage.html",{"storages":storages, "marca":marca})
    else:
        respuesta = "Che, mandame información!"
    return HttpResponse(respuesta)