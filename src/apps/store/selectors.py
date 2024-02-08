from django.db.models import QuerySet, F

from apps.store.models import LoanApplicationProduct


def get_unique_producers_selector(qs: QuerySet[LoanApplicationProduct], pk=None) -> QuerySet[tuple]:
    qs = qs.filter(loan_application_id=pk)
    qs = qs.annotate(producer_id=F('product__producer_id'))
    ids = qs.order_by('producer_id').values_list('producer_id').distinct()
    return ids
