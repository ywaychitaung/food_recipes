from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'title', 'image', 'description', 'prep_time', 'cook_time', 'serving', 'instructions', 'ingredients', 'created_at', 'updated_at')