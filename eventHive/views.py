from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from users_app.models import UserProfile
from django.http import HttpResponse
from django.contrib.auth import logout
from Course_app.models import Course
from Sponsor_app.models import ActiveSponsor

def to_index(request):
    return render(request,'index.html')


def Mainpage(request):
    allevents = Course.objects.all()
    context={
        'course':allevents
    }
    return render(request , 'index.html', context)


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


@login_required
def view_sponsors(request):
    allsponsors = ActiveSponsor.objects.all()
    context={
        'allsponsors':allsponsors
    }
    return render(request,'show_sponsors.html',context)


@login_required
def view_events(request):
    allevents = Course.objects.all()
    context={
        'course':allevents
    }
    return render(request,'show_events.html',context)



def logout_view(request):
    logout(request)
    return redirect('index')

