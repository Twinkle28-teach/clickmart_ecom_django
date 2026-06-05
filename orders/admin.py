from django.contrib import admin
from .models import Order,OrderItem

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInLine]


admin.site.register(Order,OrderAdmin)