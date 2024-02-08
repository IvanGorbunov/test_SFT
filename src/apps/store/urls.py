from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('unique-producers-of-loan-applications-products/<int:pk>/',
         views.LoanApplicationProductViewSet.as_view({'get': 'get_unique_producers', }), name='unique-producers'),
]
