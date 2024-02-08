from django.contrib import admin

from apps.store.models import (
    Producer,
    Product,
    Customer,
    LoanApplication,
    LoanApplicationProduct,
)

from utils.admin import BaseModelAdmin


@admin.register(Producer)
class ProducerAdmin(BaseModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = (
        'id',
        'name',
        'producer',
        'created_at',
    )


@admin.register(Customer)
class CustomerAdmin(BaseModelAdmin):
    pass


@admin.register(LoanApplication)
class LoanApplicationAdmin(BaseModelAdmin):
    list_display = (
        'id',
        'customer',
        'created_at',
    )
    list_display_links = (
        'id',
    )
    readonly_fields = ('created_at',)
    ordering = (
        '-id',
    )


@admin.register(LoanApplicationProduct)
class LoanApplicationProductAdmin(BaseModelAdmin):
    list_display = (
        'id',
        'loan_application',
        'product',
    )
    list_display_links = (
        'id',
        'loan_application',
    )
    readonly_fields = []
    ordering = (
        '-loan_application',
        'product',
    )
