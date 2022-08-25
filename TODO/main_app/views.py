from django.shortcuts import render,redirect
from main_app.models import TODO

# Create your views here.

def home(request):
    todos = TODO.objects.all()
    return render(request, 'home.html', {'todos':todos})


def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    else:
        title = request.POST['title']
        dis = request.POST['dis']

        TODO.objects.create(title = title, dis= dis, is_completed =False)
        return redirect('home')

def delete(request, id):
    todo= TODO.objects.get(id=id)
    todo.delete()
    return redirect('home')
    
def delete_all(request):
    TODO.objects.all().delete()
    return redirect('home')

def edit(request,id):
    todo = TODO.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'edit.html',{'todo':todo})
    else:
        ntitle = request.POST['title']
        ndis = request.POST['dis']
        todo.title = ntitle
        todo.dis = ndis
        todo.save()
        return redirect('home')

def markcompleted(request,id):
    todo = TODO.objects.get(id=id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('home')