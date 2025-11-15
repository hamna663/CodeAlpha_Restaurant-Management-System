from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="menu_images/", null=True, blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField()
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} - Seats: {self.seats}"


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    reservation_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.table.isAvailable:
            super().save(*args, **kwargs)
            self.table.isAvailable = False
            self.table.save()
        else:
            raise ValueError("Table is not available for reservation.")

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.reservation_time}"


class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=20, default="units")
    last_updated = models.DateTimeField(auto_now=True)
    threshold = models.PositiveIntegerField(default=10)

    def is_low_quantity(self):
        return self.quantity <= self.threshold

    def __str__(self):
        return f"{self.name} - {self.quantity} {self.unit}"


class Order(models.Model):
    status_choices = [
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through="OrderItem")
    status = models.CharField(max_length=20, choices=status_choices, default="PENDING")
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_total(self):
        total = sum(item.menu_item.price * item.quantity for item in self.orderitem_set.all())
        self.total_price = total
        self.save()

    def __str__(self):
        return f"Order {self.id} for Table {self.table.number}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for Order {self.order.id}"