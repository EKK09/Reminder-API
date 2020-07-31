from django.urls import path
from . import views

urlpatterns = [
    path('reminders', views.reminders),
    path('tags', views.tags),
    path('categorys', views.categorys),
]
