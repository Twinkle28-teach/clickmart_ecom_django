from django.shortcuts import render
from rest_framework import generics
from .models import Catagory,Product
from .serializers import CatagorySerializer, ProductSerializer

# Create your views here.
class CatagoryListView(generics.ListAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'