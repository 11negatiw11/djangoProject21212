from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *

class MainLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthForm
    success_url = '/'

def home(request):
    if request.GET.get('category'):
        category = Category.objects.get(pk=request.GET['category'])
        items= Item.objects.filter(category=category)
    else:
        items = Item.objects.all()

    categories = Category.objects.all()
    return render(request, 'home.html', {'items': items,'categories':categories})
def via(request):
    return render(request, 'Aboutes.html')
def fof(request):
    return render(request, 'forfrfrf.html')
def fofr(request):
    return render(request, 'fofr.html')
def konez(request):
    return render(request, 'konez.html')