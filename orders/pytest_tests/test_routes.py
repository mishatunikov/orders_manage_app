from http import HTTPStatus

import pytest
from pytest_lazyfixture import lazy_fixture


@pytest.mark.parametrize(
    'url',
    (
        lazy_fixture('homepage_url'),
        lazy_fixture('stat_url'),
        lazy_fixture('detail_order_url'),
        lazy_fixture('delete_order_url'),
        lazy_fixture('edit_order_url'),
        lazy_fixture('create_order_url'),
    ),
)
@pytest.mark.django_db
def test_pages_availability(client, url):
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
