from django.http import JsonResponse, HttpResponse
from .models.ReminderTagModel import ReminderTag
from .models.ReminderCategoryModel import ReminderCategory
from django.views.decorators.csrf import csrf_exempt
import json


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