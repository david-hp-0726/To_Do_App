from django.shortcuts import render
from .models import ListItem

# Create your views here.
def home(request):
    all_items = ListItem.objects.all
    context = {"all_items": all_items}
    return render(request, "todolist/home.html", context)

def profile(request):
    return render(request, "todolist/profile.html")

def login(request):
    return render(request, "todolist/login.html")

def signup(request):
    return render(request, "todolist/signup.html")