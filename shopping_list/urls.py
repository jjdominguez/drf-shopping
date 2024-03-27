# shopping_list/urls.py


from django.urls import include, path

from shopping_list.api.views import ListAddShoppingItem, ListAddShoppingList, ShoppingItemDetail, ShoppingListDetail

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),  # NEW!
    path("api/shopping-lists/", ListAddShoppingList.as_view(), name="all-shopping-lists"),
    path("api/shopping-lists/<uuid:pk>/", ShoppingListDetail.as_view(), name="shopping-list-detail"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/", ListAddShoppingItem.as_view(), name="list-add-shopping-item"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/<uuid:item_pk>/", ShoppingItemDetail.as_view(), name="shopping-item-detail"),
]

