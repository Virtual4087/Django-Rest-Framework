from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def api_response(request):
    return JsonResponse({"message": "Sup Nigga"})