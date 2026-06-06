from django.db import models
from decimal import Decimal

# Create your models here.
class Catagory(models.Model):
    cat_name = models.CharField(max_length=20)
    cat_desc = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return self.cat_name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,blank=True)
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=2,default=Decimal('0.00'))
    stock = models.PositiveSmallIntegerField()
    tax_percentage = models.DecimalField(max_digits=12,decimal_places=2,default=Decimal('0.00'))
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name