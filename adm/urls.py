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
from adm import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('adm/tb_adm/',views.tb_adm,name="tb_adm"),
    path('adm/info_data/',views.info_data,name="informatiquee"),
    path('adm/Energie_data/',views.energie_data,name="energiee"),
    path('adm/manag_data/',views.manag_data,name="managemante"),
    path('adm/elect_data/',views.electrique_data,name="electriquee"),
        path('adm/info_data2/',views.info_data2,name="informatiquee2"),
    path('adm/Energie_data2/',views.energie__data2,name="energiee2"),
    path('adm/manag_data2/',views.manag_data2,name="managemante2"),
    path('adm/elect_data2/',views.elect_data2,name="electriquee2"),

    path('adm/profile/',views.profile,name="profilee"),
    path('adm/tb_student/',views.tb_student,name="tb_student"),
    path('adm/tb_teacher/',views.tb_teacher,name="tb_teacher"),
    path('adm/createacc/',views.createacc,name="createacc"),
    path('adm/createstud/',views.createstud,name="createstud"),
    path('adm/createprof/',views.createprof,name="createprof"),
    path('adm/logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('adm/delete/<int:id>/',views.delete_data,name="deletedata"),
    path('adm/edit/Admin/<int:id>/',views.edit_data_admin,name="editdata_admin"),
    path('adm/edit/Student/<int:id>/',views.edit_data_stud,name="editdata_stud"),
    path('adm/edit/Teacher/<int:id>/',views.edit_data_teach,name="editdata_teach"),
    path('adm/search/', views.search_results, name='search_aa'),
        path('adm/search2/', views.search_resultsS, name='search_nn'),
    path('adm/search3/', views.search_resultsT, name='search_ww'),

    path('adm/search_inf#/', views.search_results2, name='search_info1'),
    path('adm/search_manag#/', views.search_results22, name='search_manag1'),
    path('adm/search_energ#/', views.search_results222, name='search_energ1'),
    path('adm/search_eleq#/', views.search_results2222, name='search_eleq1'),

    path('adm/search_info2#/', views.search_results3, name='search_info2'),
    path('adm/search_manag2#/', views.search_results33, name='search_manag2'),
    path('adm/search_energ2#/', views.search_results333, name='search_energ2'),
    path('adm/search_eleq2#/', views.search_results3333, name='search_eleq2'),
    path('adm/notification/', views.notif, name='notif'),
    path('adm/emploi/', views.emploi_tm,name="emploi_tm"),
    path('adm/emploi_tc/', views.emploi_tm1,name="emploi_tm1"),
    path('deleteFile/<int:id>/',views.deleteFile,name="deletedata_emp"), 
    path('adm/examens/',views.examens_adm,name="examens_adm"),
    path('deleteFile_adm/<int:id>/',views.deleteFile_adm,name="deletedata_emp_adm"), 
   

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
