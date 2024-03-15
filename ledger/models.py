from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # Arbitrary max length just to prevent the bio from being too long (it is "short" after all)
    # "min_length" does not exist so we have to use a validator
    short_bio = models.CharField(max_length=1000, validators=[MinLengthValidator(255)])

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
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ledger:recipe_detail", args=[self.id, str(self.name)])


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
