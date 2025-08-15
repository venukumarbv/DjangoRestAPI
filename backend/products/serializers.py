from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['title',
                  'content',
                  'price',
                  'sale_price',
                  "my_discount",

                  ]  # '__all__'


    # Method name should be 'get_<variable_name_defined_above>' ; get_my_discount
    def get_my_discount(self, obj): # obj is important
        return obj.get_discount() # Calling the method get_discount written in the models.py

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()