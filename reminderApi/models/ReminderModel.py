from django.db import models


class Reminder(models.Model):
    title = models.CharField(max_length=20)
    remind_time = models.DateTimeField(null=True)
    finished = models.BooleanField(default=False)
    created_date = models.DateTimeField('建立時間', auto_now_add=True)

    # TODO: 新增標籤與類別

    @staticmethod
    def getAll():
        reminders = []
        for querySet in Reminder.objects.all():
            reminder = {'id': querySet.id, 'title': querySet.title,
                        'remindTime': querySet.remind_time, 'finished': querySet.finished}
            reminders.append(reminder)

        return reminders

    @staticmethod
    def add(reminder):
        unit = Reminder.objects.create(
            title=reminder['title'], remind_time=reminder['remindTime'], finished=reminder['finished'])
        unit.save()
        return

    @staticmethod
    def deleteReminder(id):
        unit = Reminder.objects.get(id=id)
        unit.delete()
        return
