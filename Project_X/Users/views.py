from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def users(request):
    template = loader.get_template('users.html')
    return HttpResponse(template.render())

def home_profile(request):
    template = loader.get_template('home_profile.html')
    return HttpResponse(template.render())


