"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from myapp.views import add_person, my_view,book_list,index, ruby

app_name = 'admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_view/', my_view, name='my_view'),
    path('add_person/', add_person, name='add_person'),
    path('books/', book_list, name='book_list'),
    path('index/', index, name='index'),
    
]
