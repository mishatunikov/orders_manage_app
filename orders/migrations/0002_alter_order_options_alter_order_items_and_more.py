# Generated by Django 4.2.16 on 2025-01-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={
                'ordering': ('-created_at',),
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.JSONField(
                default=list,
                help_text='Поле для хранения заказанных блюд. Формат: [{"name":"Название блюда", "price": Цена (целочисленное значение)},]',
                verbose_name='Блюда',
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(
                choices=[
                    ('waiting', 'В ожидании'),
                    ('ready', 'Готово'),
                    ('paid', 'Оплачено'),
                ],
                default='waiting',
                help_text='Выберите из выпадающего списка.',
                max_length=25,
                verbose_name='Status',
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='table_number',
            field=models.IntegerField(
                help_text='Номер стола (целочисленное значение)',
                verbose_name='Номер стола',
            ),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(
                blank=True,
                help_text='Вычисляется автоматически',
                verbose_name='Стоимость заказа',
            ),
        ),
    ]
