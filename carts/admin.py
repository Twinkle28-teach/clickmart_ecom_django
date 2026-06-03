from django.contrib import admin
from .models import Cart,CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart','product','quantity']

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem,CartItemAdmin)
