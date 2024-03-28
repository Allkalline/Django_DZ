from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import logging
from datetime import datetime, timedelta
from .models import Client, Product, Order
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Главная страница была посещена {datetime.datetime.now().replace(microsecond=0)}')
    return render(request, 'myapp/index.html')


def about(request):
    logger.info(f'Страница "Обо мне" была посещена {datetime.datetime.now().replace(microsecond=0)}')
    return render(request, 'myapp/about.html')


def list_ordered(request, client_id):
    unique_products1 = set()
    unique_products2 = set()
    unique_products3 = set()
    client = Client.objects.get(pk=client_id)

    orders7 = Order.objects.filter(client=client,
                                   order_date__range=[datetime.now() - timedelta(days=7), datetime.now()])
    orders30 = Order.objects.filter(client=client,
                                    order_date__range=[datetime.now() - timedelta(days=30), datetime.now()])
    orders365 = Order.objects.filter(client=client,
                                     order_date__range=[datetime.now() - timedelta(days=365), datetime.now()])

    for order in orders7:
        unique_products1.update(order.products.all())

    for order in orders30:
        unique_products2.update(order.products.all())

    for order in orders365:
        unique_products3.update(order.products.all())

    context = {
        'client': client,
        'products1': unique_products1,
        'products2': unique_products2,
        'products3': unique_products3,
        'title': f'Заказы клиента {client.name}',
    }

    return render(request, 'myapp/list_ordered.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            photo = request.FILES['photo']

            product = Product(name=name, description=description, price=price, quantity=quantity, photo=photo)
            product.save()

            request.session['success'] = 'Продукт успешно добавлен'
            return HttpResponseRedirect('/add_product')


    else:
        form = ProductForm()
    products = Product.objects.all()

    context = {
        'form': form,
        'products': products,
        'title': 'Добавление продукта',
    }

    return render(request, 'myapp/add_product.html', context)
