from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from decimal import Decimal

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email
    @property
    def subtotal(self):
        subtotal=Decimal("0.00")
        for item in self.items.all():
            subtotal += Decimal(str(item.product.price)) * Decimal(str(item.quantity))
        return subtotal
    @property
    def tax_amount(self):
        tax = Decimal("0.00")
        for item in self.items.all():
            tax += (Decimal(str(item.product.price))* Decimal(str(item.quantity)) * Decimal(str(item.product.tax_percentage))/ Decimal("100"))
        return tax.quantize(Decimal("0.01"))
    @property
    def grand_total(self):
        total = self.subtotal + self.tax_amount
        print("SUBTOTAL =", self.subtotal)
        print("TAX =", self.tax_amount)
        print("TOTAL =", total)

        return total



    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name}*{self.quantity}"
    @property
    def total_price(self):
        total_price = Decimal(str(self.product.price)) * Decimal(str(self.quantity))
        
        return total_price