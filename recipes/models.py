from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Recipe(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(unique=True, null=True)
  image = models.ImageField(upload_to="recipes", null=True)
  description = models.TextField(null=True)
  prep_time = models.PositiveIntegerField(null=True)
  cook_time = models.PositiveIntegerField(null=True)
  serving = models.PositiveIntegerField(null=True)
  instructions = models.TextField(null=True)
  ingredients = models.TextField(null=True)

  author = models.ForeignKey(User, on_delete=models.CASCADE)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    self.slug = self.slug or slugify(self.title)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
      return reverse("recipes-home",)

  def __str__(self):
    return self.title