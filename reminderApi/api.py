from django.urls import path
from . import views

urlpatterns = [
    path('tags', views.tags),
    path('categorys', views.categorys),
]