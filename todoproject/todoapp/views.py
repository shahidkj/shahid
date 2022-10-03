from django.shortcuts import render, redirect

# Create your views here.
from todoapp.models import task


def home(request):
    new = task.objects.all()
    if request. method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        Task=task(name=name,priority=priority)
        Task.save()
    return render(request,"home.html",{'task':new})
# def detail(request)
#
#
#     return render(request,'detail.html',{'task':new})

def delete(request,id):
    Task = task.objects.get(id=id)
    if request.method=='POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')