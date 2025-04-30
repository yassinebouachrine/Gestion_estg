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
from prof import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    
    path('prof/notes_prof/', views.notes_pro,name="notes_pro"),
    path('prof/cours_prof/', views.cours_pro,name="cours_pro"),
    path('prof/profile/', views.profile,name="profile_prof"),
    path('prof/logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('deletecours/<int:id>/', views.deletecours,name="deletecours"),
    path('prof/emploi_prof/', views.emploi_prof,name="emploi_prof"),
 

]

 
 