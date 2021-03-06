"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

import employee.views
from employee.views import PersonView,PersonCreate,PersonUpdate,PersonDelete
import calc.urls
import travello.urls
# import calc.views
# from calc.views import home
print( static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calc/', include(calc.urls)),
    path('', include(travello.urls)),
    path('person/', PersonView, name='Person'),
    path('person/create/', PersonCreate, name='Create Person'),
    path('person/update/<id>', PersonUpdate, name='Update Person'), 
    path('person/delete/<id>', PersonDelete, name='Delete Person'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
