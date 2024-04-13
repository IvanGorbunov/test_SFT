from .base_views import BaseCustomerViewSet
from ..serializers.serializers_v2 import CustomerSerializer


class CustomerViewSet(BaseCustomerViewSet):
    serializers = {
        'list': CustomerSerializer,
        'create': CustomerSerializer,
        'retrieve': CustomerSerializer,
        'update': CustomerSerializer,
        'partial_update': CustomerSerializer,
    }