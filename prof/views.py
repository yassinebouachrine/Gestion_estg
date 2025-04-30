from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Cours
from .forms import coursForm, notesForm
from stud.functions import handle_uploaded_file
from adm.models import User
from stud.models import Notes

# Create your views here.


@csrf_exempt
def notes_pro(request):
    mydata = Notes.objects.all()
    dd = User.objects.all()
    form = notesForm()  # initialize form
    context = {'form': form, 'mydata': mydata, 'dd': dd}  # initialize context
    if request.method == 'POST':  
        form = notesForm(request.POST, request.FILES)  
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/prof/notes_prof')
    else:  
         form = notesForm()
        
    return render(request, 'prof/notesaffich.html', context)






@csrf_exempt
def cours_pro(request):   
    mydata = Cours.objects.all()
    if request.method == 'POST':  
        form = coursForm(request.POST, request.FILES)  
        if form.is_valid():
            handle_uploaded_file(request.FILES['cours_pdf']) 
            model_instance = form.save(commit=False, user=request.user)
            model_instance.nm_prof = request.user
            model_instance.save()
            form.save_m2m()
            return redirect('/prof/cours_prof')  
    else:  
         form = coursForm()
         context = {'form':form,'mydata':mydata}
     
    return render(request, 'prof/coursaffich.html', context)


import os

@csrf_exempt
def deletecours(request,id):
    if request.method == 'POST':
     pi = cours.objects.get(id=id)
     pi.delete()                 
     return redirect('/prof/cours_prof') 

    

from adm.models import PDFFile

def emploi_prof(request):
   mydata = PDFFile.objects.all()    
   if mydata != '':
        context = {'mydata':mydata}
        return render(request,'prof/emploi_prof.html',context)
  
   return render(request,"prof/emploi_prof.html", context) 








def profile(request):
    
    return render(request, 'prof/profile_prof.html')