# invoice/urls.py
from django.urls import path
from .views import customer_list, invoice_list, item_list

urlpatterns = [
    path('customers/', customer_list, name='customer-list'),
    path('invoices/', invoice_list, name='invoice-list'),
    path('items/', item_list, name='item-list'),
]
