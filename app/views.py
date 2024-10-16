from django.utils.timezone import now
from django.db.models import Q
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CitySerializer, StreetSerializer, ShopListSerializer, ShopCreateSerializer
from .models import City, Shop, Street


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class StreetViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = StreetSerializer

class ShopListView(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == "GET":
            return ShopListSerializer
        if self.request.method == "POST":
            return ShopCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Shop.objects.all()
        street = self.request.query_params.get('street')
        city = self.request.query_params.get('city')
        op = self.request.query_params.get('open')
        if city is not None:
            queryset = queryset.filter(city__name=city)
        if street is not None:
            queryset = queryset.filter(street__name=street)
        if op is not None:
            if op.isalpha() or int(op) not in [0, 1]:
                raise serializers.ValidationError({'error': 'Значение open должно быть 0 или 1.'})
            time_now = now().time()
            if int(op):
                queryset = queryset.filter(opening_time__lte=time_now, closing_time__gt=time_now)
            else:
                queryset = queryset.filter(Q(opening_time__gt=time_now) | Q(closing_time__lte=time_now))
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        street= Street.objects.get(pk=request.data["street"])
        city = City.objects.get(pk=request.data["city"])
        if street.city.id != city.id:
            raise serializers.ValidationError({'error': f'В городе {city.name} с id={city.pk} отсутствует улица {street.name} с id={street.pk}'})
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"id": serializer.data['id']}, status=status.HTTP_201_CREATED, headers=headers)