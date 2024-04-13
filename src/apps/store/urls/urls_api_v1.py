from django.urls import path

from .. import views

app_name = 'store-api-v1'

urlpatterns = [
    path('costomers/',
         views.CustomerViewSetV1.as_view({'get': 'list', 'post': 'create'}), name='list'),
    path('costomers/<int:pk>/', views.CustomerViewSetV1.as_view(
        {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='manage'),

]
