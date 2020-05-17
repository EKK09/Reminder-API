from django.db import models

# Create your models here.


class ReminderTag(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField('建立時間', auto_now_add=True)

    @staticmethod
    def getAll():
        tags = []
        for querySet in ReminderTag.objects.all():
            tag = {'id': querySet.id, 'name': querySet.name}
            tags.append(tag)
        return tags

    @staticmethod
    def add(name):
        unit = ReminderTag.objects.create(name=name)
        unit.save()
        return

