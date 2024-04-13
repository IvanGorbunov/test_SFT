from django.urls import path

from .. import views

app_name = 'store-api-v2'

urlpatterns = [
    path('costomers/',
         views.CustomerViewSetV2.as_view({'get': 'list', 'post': 'create'}), name='list'),
    path('costomers/<int:pk>/', views.CustomerViewSetV2.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='manage'),
]
