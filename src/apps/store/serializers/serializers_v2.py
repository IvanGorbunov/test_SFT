from rest_framework import serializers

from .base_serializers import BaseCustomerSerializer
from ..models import Customer


class CustomerSerializer(BaseCustomerSerializer):
    class Meta:
        ref_name = 'Customer v2'
        model = Customer
        fields = [
            'id',
            'name',
            'created_at',
        ]

    def get_fields(self):
        fields = super().get_fields()
        fields.update(self.get_feature_flag_fields())
        return fields

    def get_feature_flag_fields(self):
        return {
            field: serializers.BooleanField(required=False, read_only=True)
            for field in Customer.get_features_field_names()
        }
