from django.shortcuts import render

# Create your views here.

from django.conf.urls import url

 

def index(request):
    context = {
    
    
    }
    
    return render(request, 'portfolio/index.html', context) 


def Artwork(request):
    return render(request, 'portfolio/Artwork.html', {})
    
    return HttpResponse("This is a page for Artwork")

def other(request):
    name = request.POST['Name']
    
    return HttpResponse("Done")

