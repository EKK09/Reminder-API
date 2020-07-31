from django.http import JsonResponse, HttpResponse
from .models.ReminderTagModel import ReminderTag
from .models.ReminderCategoryModel import ReminderCategory
from .models.ReminderModel import Reminder
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime


@csrf_exempt
def reminders(request):
    method = request.method

    if method == 'GET':
        content = Reminder.getAll()
        # TODO: 處理還傳資料格式
        return JsonResponse(content, safe=False, charset='utf-8')

    elif method == 'POST':
        bodyUnicode = request.body.decode('utf-8')
        bodyJson = json.loads(bodyUnicode)

        addableReminder = {}
        addableReminder['title'] = bodyJson['title']
        addableReminder['remindTime'] = datetime.fromtimestamp(bodyJson[
                                                               'remindTime'])
        addableReminder['finished'] = bool(bodyJson['finished'])
        Reminder.add(addableReminder)

        return HttpResponse(status=204)

    elif method == 'DELETE':
        bodyUnicode = request.body.decode('utf-8')
        bodyJson = json.loads(bodyUnicode)
        Reminder.deleteReminder(bodyJson['id'])

        return HttpResponse(status=204)


@csrf_exempt
def tags(request):
    method = request.method

    if method == 'GET':
        content = ReminderTag.getAll()

        return JsonResponse(content, safe=False, charset='utf-8')

    elif method == 'POST':
        bodyUnicode = request.body.decode('utf-8')
        bodyJson = json.loads(bodyUnicode)
        ReminderTag.add(bodyJson['name'])

        return HttpResponse(status=204)

    elif method == 'DELETE':
        bodyUnicode = request.body.decode('utf-8')
        bodyJson = json.loads(bodyUnicode)
        ReminderTag.deleteTag(bodyJson['id'])

        return HttpResponse(status=204)


@csrf_exempt
def categorys(request):
    method = request.method

    if method == 'GET':
        content = ReminderCategory.getAll()

        return JsonResponse(content, safe=False, charset='utf-8')

    elif method == 'POST':
        bodyUnicode = request.body.decode('utf-8')
        bodyJson = json.loads(bodyUnicode)
        ReminderCategory.add(bodyJson['name'])

        return HttpResponse(status=204)

    elif method == 'DELETE':
        bodyUnicode = request.body.decode('utf-8')
        bodyJson = json.loads(bodyUnicode)
        ReminderCategory.deleteCategory(bodyJson['id'])

        return HttpResponse(status=204)
