"""AssemblyProject URL Configuration

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
from django.urls import path, include


admin.site.site_header = "தமிழன் செயலி" #தமிழன் செயலிக்கு வரவேற்கிறோம்"
admin.site.site_title = "தமிழன் செயலி" #வணக்கம் - தமிழன் செயலிக்கு"
admin.site.index_title = "தமிழன் செயலி" #தமிழன் செயலி"

urlpatterns = [

    path('admin/', admin.site.urls),
    path('eservice', include('eServiceApp.urls')),
    path('adangal', include('adangalApp.urls')),
    path('election', include('electionApp.urls')),
    path('school', include('schoolApp.urls')),
    path('party', include('partyApp.urls')),
    path('government', include('govtApp.urls')),
    path('common', include('commonApp.urls'))
]
