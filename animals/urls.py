from django.urls import path

from animals.views import index, animals, search, simulator, login, simulator_form, simulator_result

app_name = 'animals'
urlpatterns = [
    path('', animals, name='index'),
]
