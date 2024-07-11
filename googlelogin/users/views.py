from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def home(request):
    return render(request, 'home.html') # Renders the home.html template


def logout_view(request):
    logout(request)
    return redirect('/')# Redirects to the home page after logout