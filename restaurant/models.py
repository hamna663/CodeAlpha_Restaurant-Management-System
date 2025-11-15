from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')



# 🧾 Menu Item
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.name


# 🍽️ Table
class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(default=4)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} (Capacity: {self.capacity})"


# 📅 Reservation
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Check if table is available before saving
        if not self.table.is_available:
            raise ValueError("This table is not available.")
        self.table.is_available = False
        self.table.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reservation for {self.customer_name} on {self.reservation_time}"


# 📦 Inventory
class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20, default='pcs')
    threshold = models.FloatField(default=5)

    def is_low_stock(self):
        return self.quantity <= self.threshold

    def __str__(self):
        return f"{self.name} ({self.quantity}{self.unit})"


# 🛒 Order
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('completed', 'Completed'),
    ]

    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def update_total(self):
        total = sum(item.menu_item.price * item.quantity for item in self.items.all())
        self.total = total
        self.save()

    def __str__(self):
        return f"Order #{self.id} ({self.status})"


# 🧾 Order Items
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"
