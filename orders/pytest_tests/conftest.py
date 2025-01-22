import pytest

from django.urls import reverse

from orders.models import Order


@pytest.fixture(autouse=True)
def enable_access_db_for_all_tests(db):
    pass


@pytest.fixture()
def create_multiple_orders():
    orders_data = (
        (2, [{'name': 'блюдо_1', 'price': 1}], 'waiting'),
        (4, [{'name': 'блюдо_2', 'price': 2}], 'ready'),
        (6, [{'name': 'блюдо_3', 'price': 3}], 'paid'),
        (3, [{'name': 'блюдо_4', 'price': 4}], 'paid'),
    )
    for table_number, items, status in orders_data:
        order = Order(table_number=table_number, items=items, status=status)
        order.save()


@pytest.fixture
def order():
    return Order.objects.create(
        table_number=10,
        items=[
            {'name': 'паста', 'price': 459},
            {'name': 'сок яблочный', 'price': 199},
        ],
    )


@pytest.fixture
def form_data():
    return {
        'table_number': 12,
        'items[]': ['паста', 'сок апельсиновый'],
        'prices[]': ['459', '259'],
    }


# URLs.
@pytest.fixture
def homepage_url():
    return reverse('orders:homepage')


@pytest.fixture
def create_order_url():
    return reverse('orders:create')


@pytest.fixture
def edit_order_url(order):
    return reverse('orders:edit', args=(order.id,))


@pytest.fixture
def delete_order_url(order):
    return reverse('orders:delete', args=(order.pk,))


@pytest.fixture
def detail_order_url(order):
    return reverse('orders:detail', args=(order.pk,))


@pytest.fixture
def stat_url():
    return reverse('orders:stat')
