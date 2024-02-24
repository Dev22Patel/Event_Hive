from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def Mainpage(request):
    return render(request , 'index.html', {})

@login_required
def home(request):
    return render(request, "home.html", {})