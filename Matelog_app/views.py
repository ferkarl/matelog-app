from django.http import JsonResponse

def home(request):
    if request.method in ['GET', 'HEAD']:
        return JsonResponse({
            "status": "ok",
            "message": "API funcionando 🚀"
        })