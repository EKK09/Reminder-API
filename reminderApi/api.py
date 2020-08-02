from django.urls import include, path
from rest_framework import routers
from .views import ReminderTagView, ReminderCategoryView, ReminderView

router = routers.DefaultRouter()
router.register(r'tags', ReminderTagView)
router.register(r'categorys', ReminderCategoryView)
router.register(r'reminders', ReminderView)

urlpatterns = [
    path('', include(router.urls)),
]
