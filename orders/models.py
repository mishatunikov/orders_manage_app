from django.db import models


class Order(models.Model):
    STATUSES = {
        'waiting': 'В ожидании',
        'ready': 'Готово',
        'paid': 'Оплачено'
    }
    table_number = models.IntegerField(verbose_name='Номер стола',
                                       help_text='Номер стола')
    items = models.JSONField(verbose_name='Блюда')
    status = models.CharField(
        'Status',
        max_length=25,
        choices=STATUSES,
        default=STATUSES['waiting'],
    )
    total_price = models.IntegerField(verbose_name='Стоимость заказа')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    @property
    def items_names(self) -> list:
        return [item['name'] for item in self.items]

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return f'Заказ №{self.pk}'





