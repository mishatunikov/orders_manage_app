import pytest
from django.db.models import Sum

from orders.models import Order


@pytest.mark.usefixtures('create_multiple_orders')
def test_count_orders_on_homepage(client, homepage_url):
    response = client.get(homepage_url)
    assert 'object_list' in response.context
    object_list = response.context['object_list']
    assert object_list.count() == Order.objects.all().count()


@pytest.mark.usefixtures('create_multiple_orders')
def test_sort_orders_by_date_on_homepage(client, homepage_url):
    response = client.get(homepage_url)
    object_list = response.context['object_list']
    all_dates = [order.created_at for order in object_list]
    sorted_dates = sorted(all_dates, reverse=True)
    assert sorted_dates == all_dates


@pytest.mark.usefixtures('create_multiple_orders')
def test_stat_info_is_correct(client, stat_url):
    response = client.get(stat_url)
    context = response.context
    paid_orders = Order.objects.filter(status='paid')
    count_paid_orders = paid_orders.count()
    profit = paid_orders.aggregate(profit=(Sum('total_price')))['profit']
    count_waiting_orders = Order.objects.filter(status='waiting').count()
    count_ready_orders = Order.objects.filter(status='ready').count()

    assert (
        'paid_orders' in context
        and count_paid_orders == context['paid_orders'].count()
    )
    assert (
        'waiting_orders' in context
        and count_waiting_orders == context['waiting_orders'].count()
    )
    assert (
        'ready_orders' in context
        and count_ready_orders == context['ready_orders'].count()
    )
    assert 'profit' in context and profit == context['profit']
