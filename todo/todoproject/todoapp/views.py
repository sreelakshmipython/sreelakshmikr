
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from.forms import Task
from. forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'
class TaskDetailView(DetailView):
       model = Task
       template_name = 'detail.html'
       context_object_name = 'task'
class TaskUpdateView(UpdateView):
     model = Task
     template_name = 'update.html'
     context_object_name = 'task'
     fields = ('name','time','date')
     def get_success_url(self):
      return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
       name = request.POST.get('name','')
       time = request.POST.get('time','')
       date=request.POST.get('date','')
       task = Task(name=name,time=time,date=date)
       task.save()
    return render(request,'home.html',{'task1':task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,id):
    task=Task.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})
