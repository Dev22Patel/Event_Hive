from django.shortcuts import render, redirect
from .forms import CourseForm  # Make sure to import the EventForm
from django.contrib import messages  # Import messages framework to show success/error messages
from django.http import HttpResponse

def add_event(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the new event to the database
            form.save()
            # Optionally, use Django's messaging framework to send a success message
            messages.success(request, 'The event has been added successfully!')
            # Redirect to a new URL (e.g., the homepage or a 'success' page)
            return redirect('home')  # Ensure 'success' matches the actual name of your success URL in urls.py
        else:
            # Log form errors if form is not valid
            print(form.errors)
            return HttpResponse("not registered")
    else:
        # Instantiate a blank version of the form if request is not POST
        form = CourseForm()

    # If method is GET or form is invalid, render the page with the form
    return render(request, 'home.html', {'form': form})
