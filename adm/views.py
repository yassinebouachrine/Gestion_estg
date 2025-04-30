from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, login
from .forms import SignUpForm, UserCreationForm, SignUpFormstud, SignUpFormprof
from .models import User
from stud.models import suiv_serv


# Create users.

def createacc(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,"File uploaded successfully.")
            return redirect('createacc')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = SignUpForm()
    
    return render(request, 'adm/createacc.html',{'form':form})


def createstud(request):
    if request.method == "POST":
        form = SignUpFormstud(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('createacc')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = SignUpFormstud()
    
    return render(request, 'adm/createstud.html',{'form':form})


def createprof(request):
    if request.method == "POST":
        form = SignUpFormprof(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('createacc')
        else:
            for error in list(form.errors.values()):
                print(request, error)

    else:
        form = SignUpFormprof()
    
    return render(request, 'adm/createprof.html',{'form':form})




# Create affiche users.

def tb_adm(request):
    data = User.objects.all()
    
    return render(request, 'adm/tb_adm.html', {'data': data})

def tb_student(request):
    data = User.objects.all()
    
    return render(request, 'adm/tb_student.html', {'data': data})

def tb_teacher(request):
    data = User.objects.all()
    
    return render(request, 'adm/tb_teacher.html', {'data': data})

def info_data(request):
    data = User.objects.all()
    
    return render(request, 'adm/info_data1.html', {'data': data})

def energie_data(request):
    data = User.objects.all()
    
    return render(request, 'adm/Energie_data1.html', {'data': data})

def manag_data(request):
    data = User.objects.all()
    
    return render(request, 'adm/Manag_data1.html', {'data': data})

def electrique_data(request):
    data = User.objects.all()
    
    return render(request, 'adm/Electrique_data1.html', {'data': data})

def profile(request):
    
    return render(request, 'adm/profile.html')


def info_data2(request):
    data = User.objects.all()
    
    return render(request, 'adm/info_data2.html', {'data': data})


def manag_data2(request):
    data = User.objects.all()
    
    return render(request, 'adm/manag_data2.html', {'data': data})


def energie__data2(request):
    data = User.objects.all()
    
    return render(request, 'adm/energie_data2.html', {'data': data})


def elect_data2(request):
    data = User.objects.all()
    
    return render(request, 'adm/elect_data2.html', {'data': data})







# Create delete users.

def delete_data(request, id):
    if request.method == 'POST':
     pi = User.objects.get(id=id)
     pi.delete()                 
     return redirect('tb_adm') 

# def delete_data_classe(request, id_classe):
#     if request.method == 'POST':
#      pi = classe.objects.get(id_classe=id_classe)
#      pi.delete()                     
#      return redirect('tb_adm')  



# Create update users.

def edit_data_admin(request, id):
    if request.method == 'POST':
       data = User.objects.get(id=id)
       fm = SignUpForm(request.POST, instance=data)
       if fm.is_valid():
         fm.save()
         return redirect('tb_adm')
       
       else:
         data = User.objects.get(id=id)
         fm = SignUpForm(instance=data)
    

    return render(request, 'adm/edit.html', {'data': data})


def edit_data_stud(request, id):
    if request.method == 'POST':
       data = User.objects.get(id=id)
       fm = SignUpFormstud(request.POST, instance=data)
       if fm.is_valid():
         fm.save()
         return redirect('tb_student')
       
       else:
         data = User.objects.get(id=id)
         fm = SignUpFormstud(instance=data)
    

    return render(request, 'adm/edit_stud.html', {'data': data})


def edit_data_teach(request, id):
    if request.method == 'POST':
       data = User.objects.get(id=id)
       fm = SignUpFormprof(request.POST, instance=data)
       if fm.is_valid():
         fm.save()
         return redirect('tb_teacher')
       
       else:
         data = User.objects.get(id=id)
         fm = SignUpFormprof(instance=data)
    

    return render(request, 'adm/edit_teach.html', {'data': data})



# Create add 


import django_filters
from django.db.models import Q

def search_results(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)

    return render(request, 'adm/search_results.html', {'puu': puu})


def search_resultsS(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)

    return render(request, 'adm/search_results1.html', {'puu': puu})


def search_resultsT(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)

    return render(request, 'adm/search_results2.html', {'puu': puu})


 
def search_results2(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)
    
    return render(request, 'adm/search_data2.html', {'puu': puu})

def search_results22(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)
    
    return render(request, 'adm/search_data2#.html', {'puu': puu})

def search_results222(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)
    
    return render(request, 'adm/search_data2##.html', {'puu': puu})

def search_results2222(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)
    
    return render(request, 'adm/search_data2###.html', {'puu': puu})



def search_results3(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)

    return render(request, 'adm/search_data3.html', {'puu': puu})

def search_results33(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)

    return render(request, 'adm/search_data3#.html', {'puu': puu})

def search_results333(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)

    return render(request, 'adm/search_data3##.html', {'puu': puu})

def search_results3333(request):
    if request.method == "POST":
       search = request.POST.get('search') 
       puu = User.objects.filter(username__icontains=search)

    return render(request, 'adm/search_data3###.html', {'puu': puu})




from django.http import HttpResponse  
from stud.functions import handle_uploaded_file
from .forms import PDFFileForm, PDFFileForm1, examensForm
from .models import PDFFile, examens
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def emploi_tm(request):
    mydata = PDFFile.objects.all()   
    if request.method == 'POST':  
          form = PDFFileForm1(request.POST, request.FILES)  
          if form.is_valid():  
             handle_uploaded_file(request.FILES['pdf_file'])  
             model_instance = form.save(commit=False)
             model_instance.save()
             return redirect('/adm/emploi/')
    else:  
           form = PDFFileForm1()  
           context = {'form':form,'mydata':mydata}
           return render(request,"adm/emploiAD.html", context) 


@csrf_exempt
def emploi_tm1(request):
    mydata = PDFFile.objects.all()   
    if request.method == 'POST':  
          form = PDFFileForm(request.POST, request.FILES)  
          if form.is_valid():  
             handle_uploaded_file(request.FILES['pdf_file'])  
             model_instance = form.save(commit=False)
             model_instance.save()
             return redirect('/adm/emploi_tc/')
    else:  
           form = PDFFileForm()  
           context = {'form':form,'mydata':mydata}
           return render(request,"adm/emploiAD1.html", context) 



import os

@csrf_exempt
def deleteFile(request,id):
    if request.method == 'POST':
     pi = PDFFile.objects.get(id=id)
     pi.delete()                 
     return redirect('/adm/emploi/') 


@csrf_exempt
def examens_adm(request):
    mydata = examens.objects.all()   
    if request.method == 'POST':  
        form = examensForm(request.POST, request.FILES)  
        if form.is_valid():  
            handle_uploaded_file(request.FILES['conv_exam'])  
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/adm/examens/')  
    else:  
           form = examensForm()  
           context = {'form':form,'mydata':mydata}
           return render(request,"adm/examen.html", context)

@csrf_exempt
def deleteFile_adm(request,id):
    if request.method == 'POST':
     pi = examens.objects.get(id=id)
     pi.delete()                 
     return redirect('/adm/examens/') 




def notif(request):
    total = suiv_serv.objects.all().count()
    use = suiv_serv.objects.filter(type_service=1)
     

    return render(request, 'adm/notif.html', {'total': total,  'use': use})




 



    










    