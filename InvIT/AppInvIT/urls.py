from django.urls import path
from AppInvIT import views

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('desktop', views.desktops, name="Desktops"),
    path('desktopsFormulario', views.desktopFormulario, name="DesktopsFormulario"),
    path('notebooks', views.notebooks, name="Notebooks"),
    path('notebooksFormulario', views.notebookFormulario, name="NotebooksFormulario"),
    path('servers', views.servers, name="Servers"),
    path('serversFormulario', views.serverFormulario, name="ServersFormulario"),
    path('storages', views.storages, name="Storages"),
    path('storagesFormulario', views.storageFormulario, name="StoragesFormulario"),
    # Busquedas
    path('busquedaNotebook', views.busquedaNotebook, name="BusquedaNotebook"),
    path('busquedaDesktop', views.busquedaDesktop, name="BusquedaDesktop"),
    path('busquedaServer', views.busquedaServer, name="BusquedaServer"),
    path('busquedaStorage', views.busquedaStorage, name="BusquedaStorage"),
    path('buscarStorage/', views.buscarStorage),
    path('buscarServer/', views.buscarServer),
    path('buscarNotebook/', views.buscarNotebook),
    path('buscarDesktop/', views.buscarDesktop),

]

