from django.db import models

class Customer(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)  # Unique ID for each customer
    name = models.CharField(max_length=255)  # Customer's name
    email = models.EmailField()  # Customer's email address

    def __str__(self):
        return self.name  # String representation of the Customer object

class Invoice(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)  # Unique ID for each invoice
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')  # Link to Customer
    date = models.DateField()  # Date of the invoice
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the invoice

    def __str__(self):
        return f"Invoice {self.unique_id} for {self.customer.name}"  # String representation of the Invoice object

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')  # Link to Invoice
    description = models.CharField(max_length=255)  # Description of the item
    quantity = models.IntegerField()  # Quantity of the item
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per item

    def __str__(self):
        return f"{self.description} - {self.quantity} @ {self.unit_price}"  # String representation of the Item object

