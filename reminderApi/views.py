from django.http import JsonResponse
from .models import ReminderTag


def tags(request):
    method = request.method

    if method == 'GET':
        content = ReminderTag.getAll()

        return JsonResponse(content, safe=False, charset='utf-8')
