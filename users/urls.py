from django.urls import path

from users.views import login, registration, home

app_name = 'users'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('home/', home, name='home'),
]
