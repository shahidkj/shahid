from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import second


def home(request):
    obj=second.objects.all()
    return render(request,"index.html",{'result':obj})

