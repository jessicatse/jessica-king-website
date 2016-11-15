from django.shortcuts import render

# Create your views here.

from django.conf.urls import url

 

def index(request):
    context = {
    
    
    }
    
    return render(request, 'portfolio/index.html', context) 



    
def artwork(request):
    return render(request, 'portfolio/Artwork.html', {})
    
    return HttpResponse("This is a page for Artwork")


def other(request):
    name = request.POST['Name']
    
    return HttpResponse("Done")


def music(request):
    return render(request, 'portfolio/music.html', {})
    
    return HttpResponse("This is a page for music")

def youtube(request):
    return render(request, 'portfolio/youtube.html', {})
    
    return HttpResponse("This is a page for youtube")
    
    
def about(request):
    return render(request, 'portfolio/about.html', {})
    
    return HttpResponse("This is a page for about")
    
    
def gallery(request):
    return render(request, 'portfolio/gallery.html', {})
    
    return HttpResponse("This is a page for gallery")
    
    