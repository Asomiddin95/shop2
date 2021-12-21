from django.urls import path
from product.views import ProductListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name="lists")
]
