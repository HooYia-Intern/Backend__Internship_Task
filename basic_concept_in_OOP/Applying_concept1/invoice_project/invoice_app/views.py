# invoice/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer, Invoice, Item

def customer_list(request):
    customers = list(Customer.objects.values())
    return JsonResponse(customers, safe=False)

def invoice_list(request):
    invoices = list(Invoice.objects.values())
    return JsonResponse(invoices, safe=False)

def item_list(request):
    items = list(Item.objects.values())
    return JsonResponse(items, safe=False)
