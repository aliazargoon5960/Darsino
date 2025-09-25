from django.urls import path
from . import views

app_name = "cart_module"

urlpatterns = [
    path('detail/', views.CartDetailView.as_view(), name="cart_detail"),
    path('add/<int:pk>/', views.CartAddView.as_view(), name="cart_add"),
    path('delete/<str:id>/', views.CartDeleteView.as_view(), name="cart_delete"),
    path('order/add/', views.OrderCreationView.as_view(), name="order_create"),
    path('checkout/<int:pk>/', views.CheckOutView.as_view(), name='checkout'),
    path('checkout/<int:pk>/discount/', views.ApplyDiscountView.as_view(), name='apply_discount'),
]
