from django.shortcuts import render
from django.http import JsonResponse
from products.models import Product
import json

# Create your views here.

def api_response(request):
    product_data = Product.objects.all().order_by("?").first()
    data = {}
    
    if product_data:
        data['title'] = product_data.title
        data['content'] = product_data.content
        data['price'] = product_data.price
    
    return JsonResponse(data)
   