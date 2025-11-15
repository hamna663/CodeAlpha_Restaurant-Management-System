from rest_framework import serializers
from .models import MenuItem, Table, Reservation, InventoryItem, Order, OrderItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class InventoryItemSerializer(serializers.ModelSerializer):
    low_stock = serializers.SerializerMethodField()

    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'quantity', 'unit', 'threshold', 'low_stock']

    def get_low_stock(self, obj):
        return obj.is_low_stock()


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), source='menu_item', write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_id', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'table', 'status', 'total', 'created_at', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        total = 0
        for item_data in items_data:
            menu_item = item_data['menu_item']
            qty = item_data['quantity']
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=qty)
            total += menu_item.price * qty

            # Reduce inventory quantity if item exists
            try:
                inv_item = InventoryItem.objects.get(name__iexact=menu_item.name)
                inv_item.quantity = max(inv_item.quantity - qty, 0)
                inv_item.save()
            except InventoryItem.DoesNotExist:
                pass

        order.total = total
        order.save()
        return order
