from django.db import models

from orders.contants import STATUSES


class Order(models.Model):
    table_number = models.IntegerField(verbose_name='Номер стола',
                                       help_text='Номер стола')
    items = models.JSONField(verbose_name='Блюда')
    status = models.CharField(
        'Status',
        max_length=25,
        choices=STATUSES,
        default='waiting',
    )
    total_price = models.IntegerField(verbose_name='Стоимость заказа')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    @property
    def item_name_price(self) -> list:
        return [(item["name"], item["price"]) for item in self.items]

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'Заказ №{self.pk}'





