from .models.ReminderTagModel import ReminderTag
from .models.ReminderCategoryModel import ReminderCategory
from .models.ReminderModel import Reminder
from rest_framework import viewsets
from rest_framework import permissions
from reminderApi.serializers import ReminderTagSerializer, ReminderCategorySerializer, ReminderSerializer


class ReminderView(viewsets.ModelViewSet):

    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class ReminderTagView(viewsets.ModelViewSet):

    queryset = ReminderTag.objects.all()
    serializer_class = ReminderTagSerializer


class ReminderCategoryView(viewsets.ModelViewSet):

    queryset = ReminderCategory.objects.all()
    serializer_class = ReminderCategorySerializer
