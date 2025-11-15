from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from datetime import date
from restaurant.models import Order, InventoryItem
from restaurant.serializers import InventoryItemSerializer

@api_view(['GET'])
def daily_sales_report(request):
    today = date.today()
    orders = Order.objects.filter(created_at__date=today,status='COMPLETED')
    total_sales = orders.aggregate(total=Sum('total_price'))['total'] or 0.00
    report = {
        "date": today,
        "total_orders": orders.count(),
        "total_sales": total_sales,
    }
    return Response(report)

@api_view(['GET'])
def inventory_status(request):
    items = InventoryItem.objects.all()
    serializer = InventoryItemSerializer(items, many=True)
    return Response(serializer.data)
