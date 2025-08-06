import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    print(model_data)
    data = {}
    if model_data:
        # data['id'] = model_data.id # Id is automatically created by the Models
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data["price"] = model_data.price

        data = model_to_dict(model_data, fields=['title', 'price'])

    return JsonResponse(data)