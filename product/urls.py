from django.urls import path
from product.views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name="lists"),
    path('shop/', ProductDetailView.as_view(), name="shop")
]
