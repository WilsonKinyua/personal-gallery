from django.shortcuts import render
from .models import Image, Category, Location
# Create your views here.


def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Homepage'
    return render(request, 'index.html', {'images': images, 'locations': locations, 'categories': categories, 'title': title})
