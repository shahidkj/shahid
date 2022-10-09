from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ToDoForms
from fourthapp.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'new'
class taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model = Task
    template_name = 'edit.html'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('taskdetailview')



def home(request):
    new = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task1=Task(name=name,priority=priority,date=date)
        task1.save()
    return render(request,'home.html',{'new1':new})
def base(request):
   return render(request,'base.html')
# def detail(request):
#
#     return render(request,'detail.html',)

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=ToDoForms(request.POST or None,instance=task)
    if f. is_valid():
        f.save()
        return redirect('/')



    return render(request,'update.html',{'f':f,'task':task})