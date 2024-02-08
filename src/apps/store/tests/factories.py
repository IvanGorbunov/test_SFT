import factory.fuzzy
from factory.django import DjangoModelFactory

from apps.store.models import (
    Producer,
    Product,
    Customer,
)


class ProducerFactory(DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(length=150)

    class Meta:
        model = Producer


class ProductFactory(DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(length=150)
    producer = factory.SubFactory(ProducerFactory)

    class Meta:
        model = Product


class CustomerFactory(DjangoModelFactory):
    name = factory.fuzzy.FuzzyText(length=150)

    class Meta:
        model = Customer
