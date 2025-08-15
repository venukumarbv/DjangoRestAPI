from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    If GET method -> It lists the objects
    If POST method -> It Creates the objects


    If Post -> Send the data in the body

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Might set an attribute(here "Content") on the object based on the request user
    def perform_create(self, serializer):
        # Data is coming from the post request
        title = serializer.validated_data.get('title')
        price = serializer.validated_data.get("price")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title

        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    # print(Product.objects.all())
    serializer_class = ProductSerializer


# class ProductListAPIView(generics.ListAPIView):
#     """
#     Dont use this; Insted use "ListCreateView"
#     """
#     queryset = Product.objects.all()
#     # print(Product.objects.all())
#     serializer_class = ProductSerializer
