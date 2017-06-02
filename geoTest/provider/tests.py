from django.test import TestCase
from provider.models import Provider, ServiceArea
from factory.fuzzy import BaseFuzzyAttribute
from django.contrib.gis.geos import Polygon
import factory.django
from django.utils import timezone


class FuzzyPoint(BaseFuzzyAttribute):
    def fuzz(self):
        return Polygon(((10, 10), (10, 20), (20, 20), (20, 15), (10, 10)))

# factories for test


class ProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Provider
        django_get_or_create = (
            'name',
            'email',
            'phone_number',
            'language',
            'reg_date'
        )

    name = 'Some provider'
    email = 'location@mozio.com'
    phone_number = '+1234567890'
    language = 'ES-es'
    reg_date = timezone.now()


class ServiceAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceArea
        django_get_or_create = (
            'name',
            'description',
            'poly',
            'price',
            'currency',
            'provider',
            'reg_date'
        )

    name = 'Some service area'
    description = 'Service area test description'
    poly = FuzzyPoint()
    price = 100.0
    currency = '$'
    provider = ProviderFactory()
    reg_date = timezone.now()


class ProviderTest(TestCase):
    def test_create_event(self):
        # Create the provider
        provider = ProviderFactory()

        # Check we can find it
        all_providers = Provider.objects.all()
        self.assertEqual(len(all_providers), 1)
        only_provider = all_providers[0]
        self.assertEqual(only_provider, provider)

        # Check attributes
        self.assertEqual(only_provider.name, 'Some provider')


class ServiceAreaTest(TestCase):
    def test_create_event(self):
        # Create new provider
        provider = ProviderFactory()

        # Create new ServiceArea
        service_area = ServiceAreaFactory(provider=provider)

        all_service_areas = ServiceArea.objects.all()
        self.assertEqual(len(all_service_areas), 1)
        only_service_area = all_service_areas[0]
        self.assertEqual(only_service_area, service_area)

        # Check attributes
        self.assertEqual(only_service_area.name, 'Some service area')
        self.assertEqual(only_service_area.provider.name, 'Some provider')
