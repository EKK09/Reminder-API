from django.http import JsonResponse
from .models import ReminderTag


def getTags(request):
    content = ReminderTag.getAll()

    return JsonResponse(content, safe=False, charset='utf-8')
