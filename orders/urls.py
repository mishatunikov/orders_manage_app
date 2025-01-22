from django.urls import path

from orders.views import (
    OrderCreateView,
    OrderListView,
    OrderDeleteView,
    OrderUpdateView,
    OrderDetailView,
    StatisticView,
)


app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('', OrderListView.as_view(), name='homepage'),
    path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name='edit'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='delete'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='detail'),
    path('statistic/', StatisticView.as_view(), name='stat'),
]
