from django.test import TestCase
from django.urls import reverse_lazy

from apps.store.models import LoanApplication
from apps.store.tests.factories import ProducerFactory, CustomerFactory, ProductFactory


class AgentViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.producers = [ProducerFactory(name=f'Завод № {i}') for i in range(1, 11)]
        cls.products = [
            ProductFactory(name=f'Товар {i.id}', producer=i)
            for i in cls.producers
        ]
        cls.product_2 = ProductFactory(name=f'Товар 11', producer=cls.producers[0])
        cls.customers = [CustomerFactory(name=f'Контрагент № {i}') for i in range(1, 4)]
        cls.loan_application_1 = LoanApplication.objects.create(
            description='Кредитная заявка № 1',
            customer=cls.customers[0]
        )
        cls.loan_application_1.products.add(cls.products[0])
        cls.loan_application_1.products.add(cls.products[1])
        cls.loan_application_1.products.add(cls.products[2])
        cls.loan_application_1.products.add(cls.product_2)
        cls.loan_application_1.save()

    def setUp(self) -> None:
        super().setUp()

    def test_url_exists_at_desired_location(self):
        response = self.client.get(f'/api/unique-producers-of-loan-applications-products/{self.loan_application_1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse_lazy('store:unique-producers', kwargs={'pk': self.loan_application_1.id}))
        self.assertEqual(response.status_code, 200)

    def test_list_unique_producers(self):
        data = [
            self.products[0].id,
            self.products[1].id,
            self.products[2].id,
        ]

        response = self.client.get(reverse_lazy('store:unique-producers', kwargs={'pk': self.loan_application_1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.data, data)
