from rest_framework.routers import DefaultRouter
from .views import (
    MenuViewSet, TableViewSet, ReservationViewSet, InventoryItemViewSet, OrderViewSet
)

router = DefaultRouter()
router.register('menu', MenuViewSet,basename="menu")
router.register('tables', TableViewSet,basename="tables")
router.register('reservations', ReservationViewSet,basename="reservations")
router.register('inventory', InventoryItemViewSet,basename="inventory")
router.register('orders', OrderViewSet,basename="orders")

urlpatterns = router.urls
