from django.contrib import admin
from reminderApi.models.ReminderTagModel import ReminderTag
from reminderApi.models.ReminderCategoryModel import ReminderCategory
# Register your models here.
admin.site.register(ReminderTag)
admin.site.register(ReminderCategory)