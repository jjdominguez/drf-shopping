# shopping_list/urls.py


from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token  # NEW

from shopping_list.api.views import (
    ListAddShoppingItem,
    ListAddShoppingList,
    SearchShoppingItems,
    ShoppingItemDetail,
    ShoppingListAddMembers,
    ShoppingListRemoveMembers,
    ShoppingListDetail,
)

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),  # NEW!
    path('api/search-shopping-items/', SearchShoppingItems.as_view(), name="search-shopping-items"),  # NEW
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),  # NEW
    path("api/shopping-lists/", ListAddShoppingList.as_view(), name="all-shopping-lists"),
    path("api/shopping-lists/<uuid:pk>/", ShoppingListDetail.as_view(), name="shopping-list-detail"),
    path('api/shopping-lists/<uuid:pk>/remove-members/', ShoppingListRemoveMembers.as_view(), name="shopping-list-remove-members"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/", ListAddShoppingItem.as_view(), name="list-add-shopping-item"),
    path("api/shopping-lists/<uuid:pk>/shopping-items/<uuid:item_pk>/", ShoppingItemDetail.as_view(), name="shopping-item-detail"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # NEW
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),  # NEW
]

