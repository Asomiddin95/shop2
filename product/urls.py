from django.urls import path
from product.views import ProductListView,ProductDetailView

app_name = 'products'

urlpatterns = [
    path('<int:pk>/', ProductDetailView.as_view(), name="detail"),
    path('', ProductListView.as_view(), name="lists")
]
