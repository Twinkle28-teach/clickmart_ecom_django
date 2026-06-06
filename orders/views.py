from django.shortcuts import render,get_object_or_404
from rest_framework.permissions import IsAuthenticated
from carts.models import Cart
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order,OrderItem
from .serializers import OrderSerializer
from rest_framework import status
from .utils import send_order_notification
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.
class PlaceOrderView(APIView):
     # check if user is logged in
    permission_classes = [IsAuthenticated]

    def post(self,request):
    # check if cart is empty
        cart = Cart.objects.get(user=request.user)
        shipping_address = request.data.get("shipping_address")
        if not cart or cart.items.count() == 0:
            return Response("error:cart is empty")

    # create the order
        order = Order.objects.create(
            user = request.user,
            subtotal = cart.subtotal,
            tax_amount = cart.tax_amount,
            grand_total = cart.grand_total,
            status = "CONFIRMED",
        #     address = shipping_address.get("address"),
        #     phone = shipping_address.get("phone"),
        #     city = shipping_address.get("city"),
        #     state = shipping_address.get("state"),
        #     zip_code = shipping_address.get("zip_code"),
        )

    #create the order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price,
                total_price = item.total_price,
            ) 
    #clear the cart
        cart.items.all().delete()
        cart.save()

    #send a notification email
        send_order_notification(order)

    #send a response to frontend
        serializer = OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_201_CREATED )
    
class MyOrdersView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class OrderDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_object(self):
        pk = self.kwargs.get('order_id')
        order = get_object_or_404(Order,pk=pk, user=self.request.user)
        return order