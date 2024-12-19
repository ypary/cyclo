from django.shortcuts import render
from animals.models import AnimalCategory, Animal

import random

# Create your views here.

# функции - обработчики запросов = контроллеры = вьюхи

def index(request):
    context = {
        'title': 'Инсектопедия',
        'username': 'Alice'
    }
    return render(request, 'animals/index.html')

def animals(request):
    context = {
        'title': 'Каталог насекомых',
        'animals': Animal.objects.all(),
        'category': AnimalCategory.objects.all()
    }
    return render(request, 'animals/animals.html', context)

def search(request):
    context = {
        'title': 'Поиск в картотеке',
        'username': 'Alice'
    }
    return render(request, 'animals/search.html', context)

def simulator(request):
    max_i = Animal.objects.count()
    i = random.randint(1, max_i)
    context = {
        'title': 'Симулятор',
        'username': 'Alice',
        'animals': Animal.objects.all(),
        'category': AnimalCategory.objects.all(),
        #'question_id': Animal.objects.order_by('?').first().id,
        'question_name': Animal.objects.get(id=i).name,
        'question_answer': Animal.objects.get(id=i).subclass.subclass
    }
    return render(request, 'animals/simulator.html', context)

def login(request):
    context = {
        'title': 'Страница входа',
        'username': 'Alice'
    }
    return render(request, 'animals/login.html', context)