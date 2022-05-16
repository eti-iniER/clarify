from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .forms import ContentInputForm

# Create your views here.

def index(request):
    content_input_form = ContentInputForm
    if request.method == 'POST':
        content_input = ContentInputForm(request.POST)
        if content_input.is_valid():
            return HttpResponse("Yeah, you tried")
            
    return render(request, 'app/index.html', {'content_input_form':content_input_form}, RequestContext(request))

def get_input(request):
    pass
