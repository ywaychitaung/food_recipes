from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework.viewsets import ModelViewSet
from . import models
from rest_framework import generics

class RecipeListView(ListView):
  model = models.Recipe
  template_name = 'recipes/home.html'
  context_object_name = 'recipes'

# Create your views here.
def home(request):
  recipes = models.Recipe.objects.all()
  context = {
    'recipes': recipes
  }
  return render(request, 'recipes/home.html', context)

def about(request):
  return render(request, 'recipes/about.html', {'title': 'about page'})


class RecipeDetailView(DetailView):
  model = models.Recipe
  slug_url_kwarg = 'the_slug'
  slug_field = 'slug'

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = models.Recipe
  slug_url_kwarg = 'the_slug'
  slug_field = 'slug'
  success_url = reverse_lazy('recipes-home')

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

class RecipeCreateView(LoginRequiredMixin, CreateView):
  model = models.Recipe
  slug_url_kwarg = 'the_slug'
  slug_field = 'slug'
  fields = ['title', 'image', 'description', 'prep_time', 'cook_time', 'serving', 'instructions', 'ingredients']

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = models.Recipe
  slug_url_kwarg = 'the_slug'
  slug_field = 'slug'
  fields = ['title', 'slug', 'image', 'description', 'prep_time', 'cook_time', 'serving', 'instructions', 'ingredients']

  def test_func(self):
    recipe = self.get_object()
    return self.request.user == recipe.author

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer

    def get_object(self):
        return get_object_or_404(Recipe, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return Recipe.objects.filter().order_by('-updated_at')

    def perform_destroy(self, instance):
        instance.save()

class RecipeInstanceView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

