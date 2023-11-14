from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def report_viewer(request):
    template = loader.get_template('report_viewer.html')
    return HttpResponse(template.render())