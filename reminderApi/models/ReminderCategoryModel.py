from django.db import models

class ReminderCategory(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField('建立時間', auto_now_add=True)

    @staticmethod
    def getAll():
        categorys = []
        for querySet in ReminderCategory.objects.all():
            category = {'id': querySet.id, 'name': querySet.name}
            categorys.append(category)
        return categorys

    @staticmethod
    def add(name):
        unit = ReminderCategory.objects.create(name=name)
        unit.save()
        return

    @staticmethod
    def deleteCategory(id):
        unit = ReminderCategory.objects.get(id = id)
        unit.delete()
        return

