from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # "Temporary" URL, ingredients are not actually accessible
        # because the model does not have a corresponding URL in
        # ledger/urls.py, no view function in ledger/views.py,
        # and no template in the ledger/templates/ledger folder.
        return "ingredient/" + self.id + "/" + str(self.name)


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=[self.id, str(self.name)])


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
