"""AssemblyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another urlconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('/', views.crop_view),
    path('cropins', views.crop_view),
    path('varisu', views.varisu_sandrithal),
    path('varisu_temp', views.varisu_sandrithal_temp),
    path('pathiram', views.pathira_pathivu),
    path('pmfby', views.pmfby_view)
]
