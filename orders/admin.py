from django.contrib import admin

from orders.models import Order


# Переопределяем модель Order в админке.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'table_number',
        'status',
        'total_price',
        'created_at',
    )

    @admin.display(description='Заказ')
    def order_number(self, obj) -> str:
        return obj

    list_editable = (
        'table_number',
        'status',
    )
    search_fields = (
        'table_number',
        'status',
    )
    list_filter = ('created_at',)
    list_display_links = ('order_number',)
