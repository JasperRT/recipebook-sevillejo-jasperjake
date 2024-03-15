from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, Profile

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

    # Custom search field for the recipe name
    search_fields = ('name', )

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

# Registering the admin for Recipe
admin.site.register(Recipe, RecipeAdmin)

# Registering the admin for User (a Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
