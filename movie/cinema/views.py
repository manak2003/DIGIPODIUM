from django.shortcuts import render
from .models import Category, Image 


def index(request):
    categories = Category.objects.all() 
    images = Image.objects.all()        
    ctx = {
        'categories': categories,
        'images': images,
        'title' : 'Image Gallery',
    }
    return render(request, 'index.html', ctx)   
   
