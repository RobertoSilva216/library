from django.http import JsonResponse


def health_view(request):
    return JsonResponse({"message": "OK"})

