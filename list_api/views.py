from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import ShoppingList, ShoppingItem, Category
from .serializers import ShoppingListSerializer, ShoppingItemSerializer, CategorySerializer, UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

    def pre_save(self, obj):
        obj.user = self.request.user

class ShoppingItemViewSet(viewsets.ModelViewSet):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
