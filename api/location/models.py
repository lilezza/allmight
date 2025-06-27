from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class City(models.Model):
    province = models.ForeignKey(Province , on_delete=models.CASCADE , related_name='cities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.province.name})"
