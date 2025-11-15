from rest_framework import viewsets
from .models import MenuItem, Table, Reservation, InventoryItem, Order
from .serializers import (
    MenuItemSerializer, TableSerializer, ReservationSerializer,
    InventoryItemSerializer, OrderSerializer
)
from .permissions import IsAdmin,IsCustomer

class MenuViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = []  # public


class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsCustomer]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

