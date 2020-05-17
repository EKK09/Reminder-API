from django.http import JsonResponse, HttpResponse
from .models import ReminderTag
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

