from django.forms import ModelForm, ValidationError

from orders.models import Order
from orders.filters import is_text, is_number


class OrderForm(ModelForm):
    """Базовая форма для создания объекта Order."""

    class Meta:
        model = Order
        exclude = ('total_price', 'created_at')

    def clean_items(self) -> list:
        items = self.cleaned_data['items']

        for item in items:
            if not is_text(item['name']):
                raise ValidationError(
                    'Название блюда должно состоять только из букв.'
                )

            if not is_number(item['price']):
                raise ValidationError(
                    'Цена может быть представлена только целым положительным '
                    'числом.'
                )

            item['price'] = int(item['price'])
            item['name'] = item['name'].lower()

        return items
