from django.shortcuts import render
from kittens.models import Kitten

def home(request):
    return render(request, "pages/home.html", {"featured_kittens": Kitten.objects.filter(status="available", is_featured=True).select_related("breed").prefetch_related("photos")[:6]})
def about(request): return render(request, "pages/about.html")
def faq(request): return render(request, "pages/faq.html")
def contact(request): return render(request, "pages/contact.html")
