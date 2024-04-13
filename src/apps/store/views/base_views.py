from rest_framework import status
from rest_framework.response import Response

from ..models import Customer
from ..serializers.base_serializers import BaseCustomerSerializer
from utils.views import MultiSerializerViewSet


class BaseCustomerViewSet(MultiSerializerViewSet):
    queryset = Customer.objects.all()
    # filtersets = {
    #     'list': AgentsRequestFilter,
    # }
    ordering_fields = []
    permission_classes = []
    serializers = {
        'list': BaseCustomerSerializer,
        'create': BaseCustomerSerializer,
        'retrieve': BaseCustomerSerializer,
        'update': BaseCustomerSerializer,
        'partial_update': BaseCustomerSerializer,
    }

    def destroy(self, request, *args, **kwargs):
        costomers = self.get_object()
        costomers.destroy()
        return Response(status=status.HTTP_204_NO_CONTENT)
