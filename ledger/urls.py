from django.urls import path
from .views import recipes_list, recipe_detail

urlpatterns = [
    path('recipes/list', recipes_list, name="recipes_list"),
    path('recipe/<int:id>/<str:name>', recipe_detail, name="recipe_detail"),
]

app_name = 'ledger'
