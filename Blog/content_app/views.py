from django.shortcuts import render,redirect
from content_app.forms import BlogForm,EditBlogform
from content_app.models import Blog 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    blogs= Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

@login_required()
def add_blog(request):
    if request.method == 'GET':
        form=BlogForm
        return render(request,'add-blog.html',{'form':form})
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Blog.objects.create(title=title,content=content,user_id=request.user.id)
            return redirect('home')
        else:
             return render(request,'add-blog.html',{'form':form})

@login_required()
def delete_blog(request,id):
    Blog.objects.get(id=id).delete()
    return redirect(home)

@login_required()
def edit_blog(request,id):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        return redirect('404')
    if request.method == 'GET':
        form = EditBlogform(instance = blog)
        return render(request, 'edit-blog.html',{'form': form}) 
    else:
        form = EditBlogform(request.POST)
        if form.is_valid():
            blog.title = form.cleaned_data['title']
            blog.content= form.cleaned_data['content']
            blog.save()
            return redirect('home')
            
def not_found(request):
    return render(request,'404.html')



    