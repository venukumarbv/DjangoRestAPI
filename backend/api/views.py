from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hi There this is Django API response !!!"})