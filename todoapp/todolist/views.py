from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('logged_out')
    all_items = List.objects.filter(user=request.user)
    context = {'all_items': all_items, 'request': request}
    return render(request, 'todolist/home.html', context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('logged_out')
    completed_items = List.objects.filter(user=request.user, completed=True)
    incomplete_items = List.objects.filter(user=request.user, completed=False)
    num_completed_high_priority = completed_items.filter(priority = "High Priority").count()
    num_completed_medium_priority = completed_items.filter(priority = "Medium Priority").count()
    num_completed_low_priority = completed_items.filter(priority = "Low Priority").count()
    num_completed_optional = completed_items.filter(priority = "Optional").count()
    num_incomplete_high_priority = incomplete_items.filter(priority = "High Priority").count()
    num_incomplete_medium_priority = incomplete_items.filter(priority = "Medium Priority").count()
    num_incomplete_low_priority = incomplete_items.filter(priority = "Low Priority").count()
    num_incomplete_optional = incomplete_items.filter(priority = "Optional").count()
    
    context = {'request': request, 
               "num_completed_high_priority": num_completed_high_priority,
               "num_completed_medium_priority": num_completed_medium_priority,
               "num_completed_low_priority": num_completed_low_priority,
               "num_completed_optional": num_completed_optional,
               "num_incomplete_high_priority": num_incomplete_high_priority,
               "num_incomplete_medium_priority": num_incomplete_medium_priority,
               "num_incomplete_low_priority": num_incomplete_low_priority,
               "num_incomplete_optional": num_incomplete_optional}
    return render(request, 'todolist/profile.html', context)

def log_in(request):
    context = {"errors": None}
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            authenticated_user = form.get_user()
            login(request, authenticated_user)
            return redirect("home")
        else:
            context["errors"] = form.errors
            return render(request, 'todolist/log_in.html', context)
    else:
        return render(request, 'todolist/log_in.html', context)

def logged_out(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'todolist/logged_out.html')

def sign_up(request):
    context = {"errors": None}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            authenticated_user = authenticate(username=user.username, password=raw_password)
            login(request, authenticated_user)
            return redirect("home")
        
        else:
            context["errors"] = form.errors
            return render(request, 'todolist/sign_up.html', context)
    else:
        return render(request, 'todolist/sign_up.html', context)

def add_task(request):
    context = {"request": request}
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            listForm = form.save(commit=False)
            listForm.user = request.user
            listForm.save()
        else:
            print("form is not valid")
        return redirect('home')
    else:
        return render(request, 'todolist/add_task.html', context)

def delete_confirm(request, item_id):
    context = {"item_id": item_id}
    return render(request, 'todolist/delete_confirm.html', context)

def delete_task(request, item_id):
    item = List.objects.get(pk = item_id)
    item.delete()
    return redirect('home')

def switch_status(request, item_id):
    item = List.objects.get(pk = item_id)
    new_status = not item.completed
    List.objects.filter(pk = item_id).update(completed = new_status)
    return redirect('home')

# def switch_status_true(request, item_id):
#     List.objects.filter(pk = item_id).update(completed=True)
#     return redirect('home')

# def switch_status_false(request, item_id):
#     List.objects.filter(pk = item_id).update(completed=False)
#     return redirect('home')