from django.shortcuts import render, redirect
from . forms import AddTaskForm
from app.models import TaskModel
# Create your views here.

def add_task(request):
    if request.method=='POST':
        form=AddTaskForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('show')
    form=AddTaskForm()
    return render(request, './add_task.html', {'form':form})

def show_tasks(request):
    data=TaskModel.objects.filter(is_completed=False)
    return render(request, './show_tasks.html', {'data':data})

def completed_tasks(request):
    data=TaskModel.objects.filter(is_completed=True)
    return render(request, './completed_tasks.html',{'data':data})

def delete_task(request, id):
    TaskModel.objects.get(pk=id).delete()
    return redirect('show')

def completed(request, id):
    print('comleted', id)
    task=TaskModel.objects.get(pk=id)
    task.is_completed=True
    task.save()
    return redirect('completed')

def edit(request, id):
    task=TaskModel.objects.get(pk=id)
    if request.method=='POST':
        form=AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show')
    form=AddTaskForm(instance=task)
    return render(request, './add_task.html', {'form':form})