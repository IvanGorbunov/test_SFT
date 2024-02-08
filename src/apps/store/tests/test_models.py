from django.db.utils import IntegrityError
from django.test import TestCase

from apps.store.models import LoanApplication
from apps.store.tests.factories import (
    ProducerFactory,
    ProductFactory,
    CustomerFactory,
)


class ModelsTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.producers = [ProducerFactory(name=f'Завод № {i}') for i in range(1, 11)]
        cls.products = [
            ProductFactory(name=f'Товар {i.id}', producer=i)
            for i in cls.producers
        ]
        cls.customers = [CustomerFactory(name=f'Контрагент № {i}') for i in range(1, 4)]
        cls.loan_application_1 = LoanApplication.objects.create(
            description='Кредитная заявка № 1',
            customer=cls.customers[0]
        )
        cls.loan_application_1.products.add(cls.products[0])
        cls.loan_application_1.products.add(cls.products[1])
        cls.loan_application_1.products.add(cls.products[2])
        cls.loan_application_1.save()

    def test_unique_products_in_loan_applications(self):
        loan_application_2 = LoanApplication.objects.create(description='Кредитная заявка № 3', customer=self.customers[2])
        with self.assertRaises(IntegrityError):
            loan_application_2.products.add(self.products[0])
