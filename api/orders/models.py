from django.db import models
from django.conf import settings
from product.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        (0 , 'در حال پرداخت'),
        (1 , 'لغو شده'),
        (2 , 'تحویل شده'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('paid' , 'پرداخت شده'),
        ('pending' , 'در انتظار پرداخت'),
        ('failed' , 'پرداخت ناموفق'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name='orders')
    status = models.IntegerField(choices = STATUS_CHOICES , default=0)
    total_amount = models.DecimalField(max_digits=12 , decimal_places=0)
    delivery_amount = models.DecimalField(max_digits=12 , decimal_places=0)
    paying_amount = models.DecimalField(max_digits=12 , decimal_places=0)
    payment_status = models.CharField(max_length=10 ,choices = PAYMENT_STATUS_CHOICES , default='pending')
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self , *args , **kwargs):
        self.paying_amount = self.total_amount + self.delivery_amount
        super().save(*args , **kwargs)

    def __str__(self):
        return f"Order {self.id} - User:{self.user.username}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='order_items')
    price = models.DecimalField(max_digits=12 , decimal_places=0)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=12 , decimal_places= 0 , blank=True)

    def save(self , *args , **kwargs):
        self.subtotal = self.price * self.quantity
        super().save(*args , **kwargs)

    def __srt__(self):
        return f"{self.quantity} x {self.product.name} (Order {self.order.id})"