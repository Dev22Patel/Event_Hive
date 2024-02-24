from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from .forms import CustomRegistrationForm
# Assuming you have a UserProfile model that stores user roles
from .models import UserProfile

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)

            # Determine the user's role
            try:
                user_profile = UserProfile.objects.get(user=user)
                user_role = user_profile.role  # Assuming 'role' is stored in UserProfile
            except UserProfile.DoesNotExist:
                user_role = 'default_role'  # Use a default role or handle as needed

            # Store the role in the session for later use (e.g., in your views to tailor content)
            request.session['user_role'] = user_role

            return redirect('home')  # Adjust to your home URL name
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')  # Ensure you have a 'login.html' template


# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New user account created")  # Inform the user of success
            return redirect('index')  # Redirect to a new URL, adjust as necessary
        else:
            # If the form is not valid, the errors will be displayed in the form template
            print(register_form.errors)  # Optional: Log form errors
    else:
        register_form = CustomRegistrationForm()
    
    return render(request, 'register.html', {'register_form': register_form})
