from django.http import JsonResponse


def getTags(request):
    # TODO: 回傳實際資料
    aTag = {'id': 1, 'name': 'a'}
    bTag = {'id': 2, 'name': 'b'}

    response = [aTag, bTag]

    return JsonResponse(response, safe=False)
