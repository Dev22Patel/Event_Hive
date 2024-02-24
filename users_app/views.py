from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegistrationForm
from django.contrib.auth import authenticate, login as auth_login




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Assuming you have a URL named 'home'
        else:
            # logger.error(f"Failed login attempt for username: {username}") 
            messages.error(request, 'Invalid username or password.')
    return render(request, 'register.html')  # Assuming your login template is named 'login.html'


# Create your views here.
def register(request):
    if request.method== "POST":
        register_form = CustomRegistrationForm(request.POST)
        if not register_form.is_valid():
            print(register_form.errors)

        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New useraccount created"))
            return redirect('index')
    else:     
        register_form = CustomRegistrationForm()
    return render(request,'register.html',{'register_form':register_form})