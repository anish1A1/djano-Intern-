from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def Register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)    #bonding the CustomUserCreationForm  with POST
        if form.is_valid():      #we always check if the form is valid or not   it always return TRUE or FALSE
            form.save()       #if the form is valid then we save the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username = username, password = password)
            login(request,user)
            return redirect('Blog')
            messages.success(request, 'Account created successfully')
    
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentications/register.html', {"form" : form})
            

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(username= username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In Successfully!")
            return redirect("Blog")
        else:
            messages.error(request, "Invalid Credentials!") 
            return redirect('user_login')
    else:
        return render(request,'authentications/login.html',{})


def logout_user(request):
    logout(request)
    messages.info(request, "You have been Logged out!")
    return redirect('Blog')

                
            
        
            
            