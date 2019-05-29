from rest_framework import serializers

from inventory.models import ProductGroup, ProductSubGroup


class ProductGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = '__all__'

class ProductSubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubGroup
        fields = '__all__'