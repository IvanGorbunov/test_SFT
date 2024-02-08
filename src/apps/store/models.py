from django.db import models

from utils.models import CreateModelMixin


class Producer(CreateModelMixin):
    name = models.CharField('Наименование', max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'
        ordering = [
            '-created_at',
        ]

    def __str__(self) -> str:
        return f'{self.name} (Производитель)'


class Product(CreateModelMixin):
    name = models.CharField('Наименование', max_length=150, blank=True, null=True)
    producer = models.ForeignKey(
        Producer,
        verbose_name='Производитель',
        related_name='products',
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = [
            '-created_at',
        ]

    def __str__(self) -> str:
        return f'{self.name} (Товар)'


class Customer(CreateModelMixin):
    name = models.CharField('Наименование', max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'
        ordering = [
            '-created_at',
        ]

    def __str__(self) -> str:
        return f'{self.name} (Контрагент)'


class LoanApplication(CreateModelMixin):
    description = models.TextField('Описание', blank=True, null=True)
    customer = models.ForeignKey(
        Customer,
        verbose_name='Контрагент',
        related_name='loan_applications',
        on_delete=models.PROTECT,
    )
    products = models.ManyToManyField(
        Product,
        verbose_name='Товары',
        related_name='loan_applications',
        blank=True,
        through='LoanApplicationProduct',
    )

    class Meta:
        verbose_name = 'Кредитная заявка'
        verbose_name_plural = 'Кредитные заявки'
        ordering = [
            '-created_at',
        ]

    def __str__(self) -> str:
        return f'{self.description}'


class LoanApplicationProduct(models.Model):
    loan_application = models.ForeignKey(
        LoanApplication,
        verbose_name='Кредитная заявка',
        related_name='loan_applications_products',
        on_delete=models.CASCADE,
    )
    product = models.OneToOneField(
        Product,
        verbose_name='Товар',
        related_name='loan_applications_products',
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Продукт кредитной заявки'
        verbose_name_plural = 'Продукты кредитных заявок'
        ordering = [
            '-loan_application',
            'product',
        ]
