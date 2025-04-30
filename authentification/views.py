from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth


# Create your views here.



def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User = auth.authenticate(username=username, password=password)
    
        if User is not None:
            if User.role == 'STUDENT':
             auth.login(request, User)
             return redirect('services')
             

            elif User.role == 'ADMIN':
             auth.login(request, User)
             return redirect('tb_adm')
            
            elif User.role == 'TEACHER':
             auth.login(request, User)
             return redirect('/prof/notes_prof/')

       
    return render(request, 'authentification/login.html')








   