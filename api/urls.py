from django.urls import path
from users import views as UserViews
from products import views as ProductViews
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from carts import views as CartViews
from orders import views as OrderViews


urlpatterns = [
    path('register/',UserViews.RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/',UserViews.ProfileView.as_view()),

    #catagories API
    path('catagories/',ProductViews.CatagoryListView.as_view()),

    #productlist API
    path('products/',ProductViews.ProductListView.as_view()),

    #productdetail API
    path('products/<int:pk>/',ProductViews.ProductDetailView.as_view()),

    #CARTS API
    path('cart/',CartViews.CartListView.as_view()),
    path('cart/add/',CartViews.AddToCartView.as_view()),
    path('cart/items/<int:item_id>/',CartViews.ManageCartItemView.as_view()),

    #ORDERS API
    path('orders/place/',OrderViews.PlaceOrderView.as_view()),

    path('orders/',OrderViews.MyOrdersView.as_view()),

    path('orders/<int:order_id>/',OrderViews.OrderDetailView.as_view()),

]

