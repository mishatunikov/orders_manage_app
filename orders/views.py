from django.views.generic import CreateView
from django.urls import reverse_lazy

from orders.forms import OrderForm
from orders.models import Order


class OrderCreateView(CreateView):
    """Обработчик нового заказа."""

    model = Order
    form_class = OrderForm
    template_name = 'orders/create.html'
    success_url = reverse_lazy('orders:homepage')

    def form_valid(self, form):
        form.instance.total_price = sum(
            item['price'] for item in form.instance.items
        )
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        items = request.POST.getlist('items[]')
        prices = request.POST.getlist('prices[]')
        post_data[items] = [
            {'name': str(item), 'price': int(price)}
            for item, price in zip(items, prices)
        ]
        request.POST = post_data
        return super().post(request, *args, **kwargs)
