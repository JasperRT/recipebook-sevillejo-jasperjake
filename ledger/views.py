from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient

def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "ledger/recipes_list.html", ctx)

@login_required
def recipe_detail(request, id, name):
    recipe = Recipe.objects.get(name__exact=name)
    ingredients = Ingredient.objects.filter(recipe__recipe__name=name)
    ctx = {"recipe": recipe, "ingredients": ingredients}
    return render(request, "ledger/recipe_detail.html", ctx)
