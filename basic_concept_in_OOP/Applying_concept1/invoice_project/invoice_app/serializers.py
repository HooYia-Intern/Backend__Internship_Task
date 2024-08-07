from rest_framework import serializers
from .models import Customer, Invoice, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'description', 'quantity', 'unit_price']

class InvoiceSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)  # Nested serialization for items

    class Meta:
        model = Invoice
        fields = ['id', 'unique_id', 'date', 'total_amount', 'items']

class CustomerSerializer(serializers.ModelSerializer):
    invoices = InvoiceSerializer(many=True, read_only=True)  # Nested serialization for invoices

    class Meta:
        model = Customer
        fields = ['id', 'unique_id', 'name', 'email', 'invoices']
