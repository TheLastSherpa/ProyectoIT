from django.contrib import admin
from .models import *

# Registramos los modelos
admin.site.register(Notebook)
admin.site.register(Desktop)
admin.site.register(Server)
admin.site.register(Storage)