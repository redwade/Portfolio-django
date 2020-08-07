from django.shortcuts import render
from .models import Job

# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'job/home.html', {'jobs': jobs})



def about(request):
    return render(request, 'job/about.html')


def contact(request):
    return render(request, 'job/contact.html')