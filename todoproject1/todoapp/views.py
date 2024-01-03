import django.views.generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .form import todoform
from . models import todo
# Create your views here.

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Todolistview(ListView):
    model = todo
    template_name = 'home1.html'
    context_object_name = 'task'

class TodoDetailview(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = 'task'

class TodoUpdateview(UpdateView):
    model = todo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('detailview',kwargs={'pk':self.object.id})

class TodoDeleteview(DeleteView):
    model = todo
    template_name = 'delete.html'
    success_url = reverse_lazy('listview')




def add(request):
    task = todo.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        Task=todo(name=name,priority=priority,date=date)
        Task.save()
    return render(request,'home1.html',{'task':task})

# def detail(request):
#
#     return render(request,'detail.html',)

def delete(request,taskid):
    task=todo.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=todo.objects.get(id=id)
    form=todoform(request.POST or None,instance=task)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'task':task})
