import re

from django.forms import ModelForm, ValidationError

from orders.models import Order


class OrderCreationForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('total_price', 'created_at', 'status')

    def clean_items(self):
        items = self.cleaned_data['items']
        for item in items:
            if not item['name'].isalpha():
                raise ValidationError(
                    'Название блюда должно состоять только из букв.'
                )

            if not re.fullmatch(r'[1-9][0-9]*', item['price']):
                raise ValidationError(
                    'Цена может быть представлена только целым положительным '
                    'числом.'
                )

            item['price'] = int(item['price'])

        return items


class OrderEditForm(ModelForm):
    class Meta:
        model = Order
        exclude = ('total_price', 'created_at')
