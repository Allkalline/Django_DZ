from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Phone: {self.phone_number}, Address: {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}, Price: {self.price}, Quantity: {self.quantity}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Client: {self.client}, Products: {self.products}, Total Amount: {self.total_amount}, Order Date: {self.order_date}'
