from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from provider.serializers import *
from provider.models import *
from django.contrib.gis.geos import Point


class ProviderList(APIView):
    """
    List all providers.
    """

    def get(self, request, format=None):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)


class ProviderDetail(APIView):
    """
    Retrieve, update, create or delete a provider instance.
    """
    serializer_class = ProviderSerializer

    def get_object(self, pk):
        try:
            return Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        provider = self.get_object(pk)
        provider = ProviderSerializer(provider)
        return Response(provider.data)

    def put(self, request, pk, format=None):
        provider = self.get_object(pk)
        serializer = ProviderSerializer(provider, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        provider = self.get_object(pk)
        provider.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = ProviderSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceAreasList(APIView):
    """
    List all serviceAreas.
    """

    def get(self, request, format=None):
        service_areas = ServiceArea.objects.all()
        serializer = ProviderSerializer(service_areas, many=True)
        return Response(serializer.data)


class ServiceAreasDetail(APIView):
    """
    Retrieve, update, create or delete a serviceArea instance.
    """
    serializer_class = ServiceAreaSerializer

    def get_object(self, pk):
        try:
            return ServiceArea.objects.get(pk=pk)
        except ServiceArea.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        service_area = self.get_object(pk)
        service_area = ServiceAreaSerializer(service_area)
        return Response(service_area.data)

    def put(self, request, pk, format=None):
        service_area = self.get_object(pk)
        serializer = ServiceAreaSerializer(service_area, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service_area = self.get_object(pk)
        service_area.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        serializer = ServiceAreaSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FindServiceAreaArround(APIView):

    """
    Retrieve, Service area by position with format
    (lng,lat) Ex: /53.345633,-6.267014
    """

    serializer_class = ServiceAreaSerializer

    def str_to_coords(self, scords):
        coord = [float(c) for c in scords.split(',')]
        return coord

    def get_object(self, pos):
        coords = self.str_to_coords(pos)
        location = Point(coords[0], coords[1])
        try:
            areas = ServiceArea.objects.filter(poly__contains=location)
        except areas.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pos, format=None):
        service_area = self.get_object(pos)
        service_area = ServiceAreaSerializer(service_area, many=True)
        return Response(service_area.data)
