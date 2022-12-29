from django.shortcuts import render
from .models import Oils

def oils_list(request):
    oils = Oils.objects.all()
    return render(request, 'recipemaker/oils_list.html', {'oils': oils})
