import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

from products.serializers import ProductSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    # model_data = Product.objects.all().order_by("?").first()
    instance = Product.objects.all().order_by("?").first() # Model serializer way

    print(instance)
    data = {}
    if instance:
        # data['id'] = model_data.id # Id is automatically created by the Models
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data["price"] = model_data.price
        # data = model_to_dict(model_data, fields=['title', 'price'])

        data = ProductSerializer(instance).data  # Model serializer way .data is important
    return Response(data)   # DRF way
    # return JsonResponse(data)