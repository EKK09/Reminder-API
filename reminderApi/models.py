from django.db import models

# Create your models here.


class ReminderTag(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField('建立時間', auto_now_add=True)