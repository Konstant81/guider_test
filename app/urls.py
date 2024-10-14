from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, StreetViewSet, ShopViewSet


router = DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'city/<int:city_pk>/street', StreetViewSet)
router.register(r'shop', ShopViewSet)
urlpatterns = [
    path('', include(router.urls)),
    ]
