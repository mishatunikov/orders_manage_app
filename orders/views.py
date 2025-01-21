from django.views.generic import CreateView
from django.urls import reverse_lazy

from orders.forms import OrderCreationForm
from orders.models import Order


class OrderCreateView(CreateView):
    """Обработчик нового заказа."""

    model = Order
    form_class = OrderCreationForm
    template_name = 'orders/create.html'
    success_url = reverse_lazy('orders:homepage')

    def form_valid(self, form):
        form.instance.total_price = sum(
            item['price'] for item in form.instance.items
        )
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        post_data['items'] = [
            {'name': item, 'price': price}
            for item, price in zip(
                request.POST.getlist('items[]'),
                request.POST.getlist('prices[]'),
            )
        ]
        request.POST = post_data
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context['error_message'] = form.errors.values()
        context['items'] = zip(
            self.request.POST.getlist('items[]'),
            self.request.POST.getlist('prices[]'),
        )
        return self.render_to_response(context)
