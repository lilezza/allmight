from django.db import models
from django.conf import settings
from orders.models import Order


class Transactions(models.Model):
    STATUS_CHOICES = [
        ('init' , 'در حال انتظار'),
        ('success' , 'پرداخت موفق'),
        ('failed' , 'پرداخت ناموفق'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name='transactions')
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name= 'transactions')
    amount = models.DecimalField(max_digits=12 , decimal_places=0)
    token = models.CharField(max_length=255 , blank=True , null=True)
    trans_id = models.CharField(max_length=255 , blank=True , null=True)
    status = models.CharField(max_length=20 , choices=STATUS_CHOICES , default='init')
    request_from = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Transactions {self.id} - {self.status}"