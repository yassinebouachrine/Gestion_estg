
from django.shortcuts import render, redirect
from .models import Notes, services, suiv_serv
from adm.models import User
from .forms import ServiceForm
from adm.models import PDFFile



# Create your views here.


	
def service(request):
   ser = services.objects.all()

   if request.method == 'POST':
      form = ServiceForm(request.POST)
      if form.is_valid():
         form = suiv_serv.save()
      else:
         form = ServiceForm()  

   return render(request, 'stud/service.html', {'ser': ser})




from django.core.files import File
from django.http import HttpResponse


def emploi(request):
   mydata = PDFFile.objects.all()    
   if mydata != '':
        context = {'mydata':mydata}
        return render(request,'stud/temp.html',context)
  
   return render(request,"stud/temp.html", context) 
       
    

from adm.models import examens

def examen_stud(request):
   mydata = examens.objects.all()    
   if mydata != '':
        context = {'mydata':mydata}
        return render(request,'stud/examen_stud.html',context)
  
   return render(request,"stud/examen_stud.html", context) 



from .models import Notes


def notes1(request):
   note = Notes.objects.all()
   
   return render(request, 'stud/S1.html', {'note': note})

def notes2(request):
   note = Notes.objects.all()
  
   return render(request,"stud/S2.html", {'note': note})    

def notes3(request):
   note = Notes.objects.all()
  
   return render(request,"stud/S3.html", {'note': note})  

def notes4(request):
   note = Notes.objects.all()
  
   return render(request,"stud/S4.html", {'note': note})  

def notes5(request):
   note = Notes.objects.all()
  
   return render(request,"stud/S5.html", {'note': note})  

def notes6(request):
   note = Notes.objects.all()
  
   return render(request,"stud/S6.html", {'note': note})
   


from prof.models import Cours


def cours_etud(request):
   cour = Cours.objects.all()  
   
   return render(request, 'stud/cours.html', {'cour': cour})



def profile(request):
    
    return render(request, 'stud/profile_stud.html')



    







