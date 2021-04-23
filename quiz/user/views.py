from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Logged in')
            return redirect('quizdb')
        else:
            messages.add_message(request, messages.WARNING, 'No such user')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            #if user exist
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, username+' user is already exist')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, 'E-mail already exist')
                    return redirect('register')
                else:
                    #add user
                    user = User.objects.create(username=username, password=password, email=email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Account created')
                    return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, 'Password does not match repassword')
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Logged out')
        return redirect('index')
