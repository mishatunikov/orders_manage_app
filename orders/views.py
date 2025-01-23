from django.db.models import Sum
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    DetailView,
    TemplateView,
)
from django.urls import reverse_lazy, reverse

from orders.forms import OrderForm
from orders.models import Order
from orders.filters import is_text, is_number
from orders.contants import STATUSES


class OrderActionMixin:
    """Миксин для страниц действий с заказом."""

    model = Order
    template_name = 'orders/create.html'
    success_url = reverse_lazy('orders:homepage')


class OrderEditCreateMixin(OrderActionMixin):
    """Миксин для страниц редактирования и создания заказа."""

    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()
        post_data['items'] = [
            {'name': item, 'price': price}
            for item, price in zip(
                request.POST.getlist('items[]'),
                request.POST.getlist('prices[]'),
            )
        ]
        # Установка статуса по-умолчанию.
        if 'status' not in post_data:
            post_data['status'] = 'waiting'
        request.POST = post_data
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        # Передача ошибок формы.
        context['error_message'] = form.errors.values()

        context['items'] = zip(
            self.request.POST.getlist('items[]'),
            self.request.POST.getlist('prices[]'),
        )
        return self.render_to_response(context)


class StatisticView(TemplateView):
    """Страница со статистикой работы."""

    template_name = 'orders/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['paid_orders'] = Order.objects.filter(status='paid')
        if context['paid_orders']:
            context['profit'] = context['paid_orders'].aggregate(
                total_price_sum=Sum('total_price')
            )['total_price_sum']
        else:
            context['profit'] = 0
        context['waiting_orders'] = Order.objects.filter(status='waiting')
        context['ready_orders'] = Order.objects.filter(status='ready')
        return context


class OrderCreateView(OrderEditCreateMixin, CreateView):
    """Создания нового заказа."""

    pass


class OrderDeleteView(OrderActionMixin, DeleteView):
    """Удаление заказа."""

    pass


class OrderUpdateView(OrderEditCreateMixin, UpdateView):
    """Редактирование заказа."""

    def get_success_url(self):
        return reverse(
            'orders:detail', kwargs={self.pk_url_kwarg: self.object.pk}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['items'] = [
            (item['name'], item['price']) for item in self.object.items
        ]
        return context


class OrderListView(ListView):
    """Главная страница."""

    template_name = 'orders/homepage.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = context['object_list']
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        flipped_statuses = {val.lower(): key for key, val in STATUSES}

        # Обработка поискового запроса в случае если он был.
        if search := self.request.GET.get('search'):
            if is_text(search):
                queryset = queryset.filter(
                    status=flipped_statuses.get(search.lower())
                )

            elif is_number(search):
                queryset = queryset.filter(table_number=int(search))

        return queryset


class OrderDetailView(DetailView):
    """Страница отдельного заказа."""

    template_name = 'orders/detail.html'
    model = Order
