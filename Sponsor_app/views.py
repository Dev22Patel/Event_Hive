from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ActiveSponsorForm  # Ensure this is imported correctly
from django.contrib import messages  # Import messages framework for success/error messages

def add_active_sponsor(request):
    if request.method == 'POST':
        form = ActiveSponsorForm(request.POST)
        if form.is_valid():
            # Save the new sponsor to the database
            form.save()
            # Optionally, use Django's messaging framework to send a success message
            messages.success(request, 'The sponsor has been added successfully!')
            # Redirect to a new URL (e.g., a 'success' page or the homepage)
            return redirect('home')  # Make sure 'home' matches the actual name of your success URL in urls.py
        else:
            # If the form is not valid, render the form again with error messages
            # Log form errors if form is not valid
            print(form.errors)
            return HttpResponse("not registered")   
    else:
        # Instantiate a blank version of the form if the request is GET
        form = ActiveSponsorForm()

    # If the method is GET or the form is invalid, render the page with the form
    return render(request, 'sponsor_app/add_sponsor.html', {'form': form})
