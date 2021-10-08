from django.shortcuts import render
from .models import Image, Category, Location
# Create your views here.


def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Homepage'
    return render(request, 'index.html', {'images': images, 'locations': locations, 'categories': categories, 'title': title})


def search(request):
    if 'category' in request.GET and request.GET["category"]:
        # change the search to be in lowercase
        search_term = request.GET.get("category").lower()
        searched_images = Image.filter_by_category(search_term)
        message = f"{search_term}"
        locations = Location.objects.all()

        return render(request, 'search.html', {"message": message, "images": searched_images, 'locations': locations})

    else:
        locations = Location.objects.all()
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, 'locations': locations})
