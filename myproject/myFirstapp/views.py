
import pathlib
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import BlogForm
from .models import *

this_dir = pathlib.Path(__file__).resolve().parent

# Create your views here.

# def home_page_view(request, *args, **kwargs):
#     print(this_dir)
    
#     pass


def firstfun(request):
    title = "My App"
    # To know how many times the page is visited
    qs = Page_Vist.objects.all()
    print(this_dir)
    page_filter = Page_Vist.objects.filter(title=request.path)
    
    try:
        percent = (page_filter.count() * 100.0)/ qs.count()
    except:
        percent = 0
    
    context ={
        "title" : title,
        "percent" : percent,
        "qs" : qs.count(),
        "page_filter" : page_filter.count()
    }            
    Page_Vist.objects.create(title=request.path)
    
    return render(request, 'myFirstapp/firstpage.html', context)


def blog(request):
    blog_posts = Blog.objects.all()
    return render(request, 'myFirstapp/blog.html', {'blog_posts':blog_posts })

def one_blog(request, blog_id):
    blog_post = Blog.objects.get(id=blog_id)
    pass


@login_required
def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
            #saving the create value inside the Blog table
        Blog.objects.create(title=title, sub_title=sub_title, description= description, image=image)
        messages.success(request, "You created a blog")
        return redirect('Blog')
    return render(request, 'myFirstapp/create_blog.html')        
            
    
# def create_blog(request):
#     if request.method == 'POST':   
#         form = BlogForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('create_blog')
#     else:
#         form = BlogForm()
    
#     return render(request, 'myFirstapp/create_blog.html', {'form': form})
         

@login_required
def update_blog(request, b_id):
    
    blog = Blog.objects.get(id=b_id)
    if request.method == "POST":
        title = request.POST.get('title')
        sub_title = request.POST.get('sub_title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        #updateing the values
        blog.title =title
        blog.sub_title = sub_title
        blog.description = description
        blog.image = image
        
        blog.save()
        messages.success(request, "The Blog has been updated!..")
        return redirect('Blog')
    return render(request, 'myFirstapp/update_blog.html', {'blog': blog} )
          
@login_required        
def delete_blog(request, b_id):
    blog = Blog.objects.get(id=b_id)
    blog.delete()
    messages.success(request, "The Blog has been deleted!..")
    return redirect('Blog')    


