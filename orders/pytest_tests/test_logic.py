from http import HTTPStatus

import pytest
from pytest_django.asserts import assertRedirects

from orders.models import Order


def test_user_can_create_order(
    client, create_order_url, homepage_url, form_data
):
    Order.objects.all().delete()
    response = client.post(create_order_url, form_data)
    assertRedirects(response, homepage_url)
    assert Order.objects.count() == 1


def test_user_can_delete_order(client, delete_order_url, homepage_url, order):
    orders_count_before = Order.objects.count()
    response = client.post(delete_order_url)
    orders_count_after = Order.objects.count()
    assertRedirects(response, homepage_url)
    assert orders_count_after + 1 == orders_count_before
    assert not Order.objects.filter(id=order.id).exists()


def test_user_can_edit_order(
    client, edit_order_url, detail_order_url, order, form_data
):
    form_data.update({'status': 'ready'})
    response = client.post(edit_order_url, form_data)
    new_order_items_as_db = [
        {'name': item, 'price': int(price)}
        for item, price in zip(form_data['items[]'], form_data['prices[]'])
    ]
    order.refresh_from_db()
    assertRedirects(response, detail_order_url)
    assert new_order_items_as_db == order.items
    assert order.status == 'ready'


@pytest.mark.parametrize(
    'search, expected_status_model',
    (('в ожидании', 'waiting'), ('готово', 'ready'), ('оплачено', 'paid')),
)
@pytest.mark.usefixtures('create_multiple_orders')
def test_user_can_search_orders_by_status(
    client, homepage_url, search, expected_status_model
):
    response = client.get(homepage_url, data={'search': search})
    assert response.status_code == HTTPStatus.OK
    assert 'object_list' in response.context

    for order in response.context['object_list']:
        assert order.status == expected_status_model


@pytest.mark.usefixtures('create_multiple_orders')
def test_user_can_search_orders_by_table_number(client, homepage_url):
    last_order = Order.objects.last()
    response = client.get(
        homepage_url, data={'search': last_order.table_number}
    )
    assert response.status_code == HTTPStatus.OK
    assert 'object_list' in response.context

    for order in response.context['object_list']:
        assert order.table_number == last_order.table_number
