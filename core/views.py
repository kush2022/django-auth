from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from . forms import NewUserForm


# Create your views here.
def home(request):
    return render(request, 'home.html')



# Register Page 
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        # error message
    
    form = NewUserForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)
        
    
# login request 
def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,  password=password)
            if user is not None:
                login(request, user)
                # message
                return redirect('home')
            else:
                pass
        else:
            pass
    form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout_request(request):
    logout(request)
    return redirect('home')