from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    # Custom search field for the recipe name
    search_fields = ('name', )

# Registering the admin for Recipe
admin.site.register(Recipe, RecipeAdmin)
