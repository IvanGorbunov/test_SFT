from rest_framework import status
from rest_framework.response import Response


from apps.store.models import LoanApplicationProduct

from apps.store.selectors import get_unique_producers_selector
from utils.views import MultiSerializerViewSet


class LoanApplicationProductViewSet(MultiSerializerViewSet):
    queryset = LoanApplicationProduct.objects.all()

    def get_unique_producers(self, request, pk, *args, **kwargs):
        unique_producers = get_unique_producers_selector(qs=self.get_queryset(), pk=pk)
        unique_producers_ids = [unique_id[0] for unique_id in unique_producers]
        return Response(unique_producers_ids, status=status.HTTP_200_OK)
