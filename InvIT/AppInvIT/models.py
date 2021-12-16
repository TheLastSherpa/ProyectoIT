from django.db import models

class Notebook(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    numeroSerie = models.CharField(max_length = 30)

    def __str__(self):
        return f"MARCA: {self.marca} ---> MODELO: {self.modelo} ---> AÑO DE FABRICACION: {self.numeroSerie}"

class Desktop(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    numeroSerie = models.CharField(max_length = 30)

    def __str__(self):
        return f"MARCA: {self.marca} ---> MODELO: {self.modelo} ---> AÑO DE FABRICACION: {self.numeroSerie}"

class Server(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    numeroSerie = models.CharField(max_length = 30)
    esRackeable = models.BooleanField()

    def __str__(self):
        return f"MARCA: {self.marca} ---> MODELO: {self.modelo} ---> AÑO DE FABRICACION: {self.numeroSerie} ---> ES RACKEABLE: {self.esRackeable}"

class Storage(models.Model):
    marca = models.CharField(max_length = 30)
    modelo = models.CharField(max_length = 30)
    numeroSerie = models.CharField(max_length = 30)
    almacenamiento = models.IntegerField()
    esRackeable = models.BooleanField()

    def __str__(self):
        return f"MARCA: {self.marca} ---> MODELO: {self.modelo} ---> AÑO DE FABRICACION: {self.numeroSerie} ---> ALMACENAMIENTO: {self.almacenamiento}TB ---> ES RACKEABLE: {self.esRackeable}"
