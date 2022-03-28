from rest_framework import serializers
from core.models import Item, List


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','name','done']

class ListSerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ['id','name','owner','item_set']