from django.db import models

# Create your models here.

#models = таблицы

class AnimalCategory(models.Model):
    subclass = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Подкласс: {self.subclass}'

class Animal(models.Model):
    name = models.CharField(max_length=128, unique=True)
    name_l = models.CharField(max_length=128, unique=True)
    subclass = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE)
    squad = models.CharField(max_length=128)
    home = models.TextField(null=True, blank=True)
    food = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='animals_images')

    def __str__(self):
        return f'Насекомое: {self.name} | Латинское наименование: {self.name_l} | Подкласс: {self.subclass.subclass}'
