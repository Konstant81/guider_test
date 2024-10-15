from django.urls import path
from .views import CityViewSet, StreetViewSet, ShopListView


urlpatterns = [
    path('shop/', ShopListView.as_view({'get': 'list', 'post':'create'})),
    path('city/', CityViewSet.as_view({'get': 'list'})),
    path('city/<int:pk>/street/', StreetViewSet.as_view({'get': 'retrieve'}))
    ]
