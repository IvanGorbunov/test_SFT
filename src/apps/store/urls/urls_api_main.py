from django.urls import path, include

from .. import views

app_name = 'store'

urlpatterns = [
    path('unique-producers-of-loan-applications-products/<int:pk>/',
         views.LoanApplicationProductViewSet.as_view({'get': 'get_unique_producers', }), name='unique-producers'),

    path('v1/', include('apps.store.urls.urls_api_v1')),
    path('v2/', include('apps.store.urls.urls_api_v2')),
]
