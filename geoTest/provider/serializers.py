from rest_framework import serializers
from provider.models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone_number',
                  'language', 'reg_date')
        read_only_fields = ('id',)


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ('id', 'name', 'description', 'poly',
                  'price', 'currency', 'reg_date', 'provider')
        read_only_fields = ('id',)
