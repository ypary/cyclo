from django.db.models.expressions import result
from django.shortcuts import render
from animals.models import AnimalCategory, Animal
from django.core.serializers import serialize
from django.db.models import Q

import random, json

# Create your views here.

# функции - обработчики запросов = контроллеры = вьюхи

def index(request):
    context = {
        'title': 'Инсектопедия',
        'username': 'Alice'
    }
    return render(request, 'animals/index.html')

def animals(request):
    # Получаем данные из базы данных
    context = {
        'title': 'Каталог насекомых',
        'animals': Animal.objects.all(),
        'category': AnimalCategory.objects.all()
    }

    # Преобразуем QuerySet в JSON-совместимый формат
    category_json = serialize('json', AnimalCategory.objects.all())
    animals_json = serialize('json', Animal.objects.all())

    # Добавляем JSON-данные в контекст
    context['category_json'] = category_json
    context['animals_json'] = animals_json

    return render(request, 'animals/animals.html', context)

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Animal.objects.filter(Q(name__contains=query)|Q(name_l__contains=query)|Q(subclass__subclass__contains=query))
    context = {
        'title': 'Поиск в картотеке',
        'username': 'Alice',
        'results': results,
        'query': query
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

def new_simulator(request):
    context = {
        'title': 'Страница входа',
        'username': 'Alice'
    }
    result = None
    if request.method == 'POST':
        try:
            n1 = float(request.POST['n1'])
            n2 = float(request.POST['n2'])
            n3 = float(request.POST['n3'])
            result = n1 + n2 + n3
        except ValueError:
            result = 'F'
        context['result'] = int(result)
    return render(request, 'animals/new_simulater.html', context)