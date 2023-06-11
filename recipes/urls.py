from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from recipes.views import RecipeViewSet
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    path('recipe/create', views.RecipeCreateView.as_view(), name="recipes-create"),
    path('recipe/<slug:the_slug>', views.RecipeDetailView.as_view(), name="recipes-detail"),
    path('recipe/<int:pk>/update', views.RecipeUpdateView.as_view(), name="recipes-update"),
    path('recipe/<int:pk>/delete', views.RecipeDeleteView.as_view(), name="recipes-delete"),
    path('about/', views.about, name="recipes-about"),

    # the URLs for your APIs start from here
    url(r'^recipe$', RecipeViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }
    )),
    url(r'^recipes$', RecipeViewSet.as_view(
        {
            'get': 'list',
        }
    )),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)