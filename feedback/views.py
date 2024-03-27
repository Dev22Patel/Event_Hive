from django.shortcuts import redirect, render  
from feedback.forms import reviewform  
from .models import Review 
from django.contrib.auth.decorators import login_required

@login_required
def feedback(request):  
    if request.method == 'POST':  
        form = reviewform(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'feedback.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = reviewform()  
  
    return render(request, 'feedback.html', {'form': form}) 


def show_review(request):
    c=Review.objects.all()
    context={
        "images":c,
    }
    return render(request,'index.html',context)