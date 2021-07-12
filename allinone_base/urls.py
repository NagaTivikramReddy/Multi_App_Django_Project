"""allinone_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'main'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.CustomRegister.as_view(), name='register'),
    path('', views.index, name='index'),
    path('unitconvertor/', include('unitconvertor.urls', namespace='unitconverter')),
    path('todolist/', include('todolist.urls', namespace='todolist')),
    path('weather/', include('weather.urls', namespace='weather')),
    path('todolist/api/', include('todoapi.urls')),

]