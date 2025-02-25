"""
URL configuration for cyclo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from animals.views import index, animals, search, simulator, login, new_simulator, simulator_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('animals/', include('animals.urls', namespace='animals')),
    path('search/', search, name='search'),
    path('simulator/', simulator, name='simulator'),
    path('login/', login, name='login'),
    path('users/', include('users.urls', namespace='users')),
    path('new_simulator/', new_simulator, name='new_simulator'),
    #path('simulator_form/', simulator_form, name='simulator_form'),  # Страница с формой
    path('simulator_result/', simulator_result, name='simulator_result'),  # Страница с результатами
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)