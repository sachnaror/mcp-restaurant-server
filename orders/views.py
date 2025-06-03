from datetime import timedelta

from django.utils import timezone
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['get'])
    def recent(self, request):
        past_hours = int(request.query_params.get('hours', 2))
        cutoff_time = timezone.now() - timedelta(hours=past_hours)
        recent_orders = Order.objects.filter(timestamp__gte=cutoff_time)
        serializer = self.get_serializer(recent_orders, many=True)
        return Response(serializer.data)
