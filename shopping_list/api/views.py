# shopping_list/api/views.py


from rest_framework import generics

from shopping_list.api.serializers import ShoppingItemSerializer, ShoppingListSerializer
from shopping_list.models import ShoppingItem, ShoppingList
import logging

logger = logging.getLogger(__name__)


class ListAddShoppingList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class ShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer


class AddShoppingItem(generics.CreateAPIView):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

    def post(self, request, *args, **kwargs):
        logger.debug("Received POST request to AddShoppingItem view.")
        logger.debug(f"Request data: {request.data}")
        logger.debug(f"URL kwargs: {kwargs}")
        return super().post(request, *args, **kwargs)


class ShoppingItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer
    lookup_url_kwarg = "item_pk"
