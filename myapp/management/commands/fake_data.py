from django.core.management.base import BaseCommand
from myapp.models import Client, Product, Order
from faker import Faker
from random import randint


faker = Faker('ru_RU')

class Command(BaseCommand):

    help = 'Create fake data'



    #def add_arguments(self, parser):
        #parser.add_argument('clients', type=int, help='Number of clients')
        #parser.add_argument('products', type=int, help='Number of products')
        #parser.add_argument('orders', type=int, help='Number of orders')

    def handle(self, *args, **kwargs):
        #clients = kwargs['clients']
        #products = kwargs['products']
        #orders = kwargs['orders']

        for _ in range(1, 6):
            rand_client = Client.objects.get(pk=randint(47, 51))
            total_amount = 1
            order = Order(client=rand_client, total_amount=total_amount)

            order.save()

            for _ in range(1, randint(1, 10)):
                rand_product = Product.objects.get(pk=randint(9, 18))
                total_amount += rand_product.price
                order.products.add(rand_product)

            total_amount -= 1
            order.total_amount = total_amount
            order.save()
        self.stdout.write(f'Rand_client: {rand_client}\nTotal_amount: {total_amount},\nrand_product: {rand_product}')




        # for i in range(products):
        #     product = Product(
        #         name = f'Product {i}',
        #         description = f'Description {i}',
        #         price = randint(100, 1000),
        #         quantity = randint(1, 10)
        #     )
        #
        #     product.save()
        #
        # self.stdout.write(self.style.SUCCESS('Successfully created products'))











