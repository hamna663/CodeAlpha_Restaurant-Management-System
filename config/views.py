from rest_framework.decorators import action
from restaurant.permissions import IsAdmin
from rest_framework.response import Response
from django.db.models import Sum
from datetime import date
from restaurant.models import InventoryItem, Order
from rest_framework.viewsets import ViewSet

class ReportsView(ViewSet):
    permission_classes = [IsAdmin]
    
    @action(methods=["GET"], detail=False)
    def daily_sales_report(request):
        today = date.today()
        sales = Order.objects.filter(created_at__date=today, status="completed")
        total_sales = sales.aggregate(total=Sum("total"))["total"] or 0
        return Response(
            {
                "date": today,
                "total_sales": total_sales,
                "orders_completed": sales.count(),
            }
        )

    @action(methods=["GET"], detail=False)
    def low_stock_alerts(request):
        low_items = [
            item.name for item in InventoryItem.objects.all() if item.is_low_stock()
        ]
        return Response({"low_stock_items": low_items, "count": len(low_items)})
