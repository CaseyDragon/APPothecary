from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Oils, Additives, Recipes
from .forms import CreateNewRecipe

def home(response):
    return render(response, 'recipemaker/home.html', {})

def lye_calc(response):
    if response.method == 'POST':
        form = CreateNewRecipe(response.POST)
        if form.is_valid():
            calc = form.cleaned_data["name"]
            recipe = Recipes(name=calc)
            recipe.save()
        return HttpResponseRedirect('/%i' %recipe.id)
    else:    
        form = CreateNewRecipe()
    return render(response, 'recipemaker/lye_calc.html', {'form':form})

def oils_list(request):
    oils = Oils.objects.all()
    return render(request, 'recipemaker/oils_list.html', {'oils': oils})

def oils_detail(request, id):
    oil = Oils.objects.get(id=id)
    return render(request, 'recipemaker/oils_detail.html', {'oil': oil})

def additives_list(request):
    additives= Additives.objects.all()
    return render(request, 'recipemaker/additives_list.html', {'additives': additives})

def additives_detail(request, id):
    additive = Additives.objects.get(id=id)
    return render(request, 'recipemaker/additives_detail.html', {'additive': additive})

def my_recipes(response):
    recipes = Recipes.objects.all()
    return render(response, 'recipemaker/my_recipes.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = Recipes.objects.get(id=id)
    return render(request, 'recipemaker/recipe_detail.html', {'recipe': recipe})

def volume_calc(response):
    return render(response, 'recipemaker/volume_calc.html', {})

def basic_formulations(response):
    return render(response, 'recipemaker/basic_formulations.html', {})