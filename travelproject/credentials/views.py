from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['passwor1']
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save();
        print("user created")
    return render(request, "register.html")

