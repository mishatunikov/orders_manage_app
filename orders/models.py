from django.db import models

from orders.contants import STATUSES


class Order(models.Model):
    """Модель заказа."""

    table_number = models.IntegerField(
        verbose_name='Номер стола',
        help_text='Номер стола ' '(целочисленное значение)',
    )
    items = models.JSONField(
        verbose_name='Блюда',
        help_text='Поле для хранения заказанных блюд. '
        'Формат: '
        '[{"name":"Название блюда", '
        '"price": Цена (целочисленное значение)},]',
        default=list,
    )
    status = models.CharField(
        'Status',
        max_length=25,
        choices=STATUSES,
        default='waiting',
        help_text='Выберите из выпадающего списка.',
    )
    total_price = models.IntegerField(
        verbose_name='Стоимость заказа',
        help_text='Вычисляется автоматически',
        blank=True,
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        # Для автоматического расчета стоимости заказа.
        self.total_price = sum(item['price'] for item in self.items)
        super().save(*args, **kwargs)

    @property
    def item_name_price(self) -> list:
        """Представляет данные items в удобно для работы в шаблоне виде."""
        return [(item["name"], item["price"]) for item in self.items]

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.pk}'
