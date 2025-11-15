from rest_framework.routers import DefaultRouter
from .views import (
    MenuItemViewSet,
    TableViewSet,
    OrderViewSet,
    OrderItemViewSet,
    ReservationViewSet,
    InventoryItemViewSet
)

router = DefaultRouter()
router.register(r'menu-items', MenuItemViewSet)
router.register(r'tables', TableViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'inventory-items', InventoryItemViewSet)

urlpatterns = router.urls
