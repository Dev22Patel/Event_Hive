from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users_app.models import UserProfile


def Mainpage(request):
    return render(request , 'index.html', {})
def success(request):
    return render(request , 'success.html', {})


@login_required
def home(request):
    user = request.user
    user_role = 'No role assigned'  # Default message if the user has no role
    try:
        user_profile = UserProfile.objects.get(user=user)
        user_role = user_profile.role
    except UserProfile.DoesNotExist:
        pass  # You can handle users without a profile differently if needed

    return render(request, 'home.html', {'username': user.username, 'user_role': user_role})