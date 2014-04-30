from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ShoppingList, ShoppingItem, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    shopping_lists = serializers.HyperlinkedRelatedField(many=True, view_name='shoppinglist-detail')

    class Meta:
        model = User
        fields = ('url', 'username', 'shopping_lists')

class ShoppingListSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.Field(source='user.username')
    shopping_items = serializers.HyperlinkedRelatedField(many=True, view_name='shoppingitem-detail')

    class Meta:
        model = ShoppingList
        fields = ('url', 'name', 'shopping_items')

class ShoppingItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ShoppingItem
        fields = ('url', 'name', 'shopping_list', 'category')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    shopping_items = serializers.HyperlinkedRelatedField(many=True, view_name='shoppingitem-detail')

    class Meta:
        model = Category
        fields = ('url', 'name', 'shopping_items')
