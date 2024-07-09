
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def firstfun(request):
    return render(request, 'myFirstapp/firstpage.html')


def blog(request):
    blog_posts = Blog.objects.all()
    return render(request, 'myFirstapp/blog.html', {'blog_posts':blog_posts })

def one_blog(request, blog_id):
    blog_post = Blog.objects.get(id=blog_id)
    pass

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
            #saving the create value inside the Blog table
        Blog.objects.create(title=title, sub_title=sub_title, description= description, image=image)
        messages.success(request, "You created a blog")
        return redirect('create_blog')
    return render(request, 'myFirstapp/create_blog.html')        
            
    


def update_blog(request, b_id):
    
    blog = Blog.objects.get(id=b_id)
    if request.method == "POST":
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        blog.title =title
        blog.sub_title = sub_title
        blog.description = description
        blog.image = image
        
        blog.save()
        messages.success(request, "The Blog has been updated!..")
        return redirect('Blog')
    return render(request, 'myFirstapp/update_blog.html', {'blog': blog} )
          
        
def delete_blog(request, b_id):
    blog = Blog.objects.get(id=b_id)
    blog.delete()
    messages.success(request, "The Blog has been deleted!..")
    return redirect('Blog')    