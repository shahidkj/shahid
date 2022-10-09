
from django.shortcuts import render

# Create your views here.
from .models import Place


def home(request):
    obj=Place.objects.all()

    return render(request,"index.html",{'result':obj})
