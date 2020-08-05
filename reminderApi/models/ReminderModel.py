from django.db import models
from .ReminderCategoryModel import ReminderCategory


class Reminder(models.Model):
    title = models.CharField(max_length=20)
    remind_time = models.DateTimeField(null=True)
    finished = models.BooleanField(default=False)
    category = models.ForeignKey(
        ReminderCategory, null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(
        '建立時間', auto_now_add=True)

    # TODO: 新增標籤
