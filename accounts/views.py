from django.shortcuts import render,redirect
from django.contrib.auth.models import user,auth

# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['Firstname']
        last_name=request.POST['Lastname']
        username=request.POST['Username']
        password1=request.POST['psw']
        password2=request.POST['psw-repeat']
        email=request.POST['email']
        user=User.objects.create_user(Username=username,psw=password1,email=email,Firstname=first_name,Lastname=last_name)
        user.save()
        print("user created")
        return redirect('/')
    else:
        return render(request,'register.html')