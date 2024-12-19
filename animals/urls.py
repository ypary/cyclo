from django.urls import path

from animals.views import index, animals, search, simulator, login

app_name = 'animals'
urlpatterns = [
    path('', animals, name='index')
]
