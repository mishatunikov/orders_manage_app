from django.forms import ModelForm

from orders.models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('total_price', 'created_at', 'status')



