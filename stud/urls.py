"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from stud import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('stud/services/', views.service,name="services"),
    path('stud/temp_emp/', views.emploi,name="emploi"),
    path('stud/examen_stud/', views.examen_stud,name="examen_stud"),
    path('stud/notes1/', views.notes1,name="notes1"),
    path('stud/notes2/', views.notes2,name="notes2"),
    path('stud/notes3/', views.notes3,name="notes3"),
    path('stud/notes4/', views.notes4,name="notes4"),
    path('stud/notes5/', views.notes5,name="notes5"),
    path('stud/notes6/', views.notes6,name="notes6"),
    path('stud/cours/', views.cours_etud,name="cours_etud"),
    path('stud/profile/', views.profile,name="profile"),
    path('stud/logout/',auth_views.LogoutView.as_view(),name="logout"),

]





