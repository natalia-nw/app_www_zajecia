from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer
from rest_framework.views import APIView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class OsobaList(APIView):

    def get(self, request, format=None):
        osoby = Osoba.objects.all()
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)


class OsobaDetail(APIView):

    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        osoba = self.get_object(pk)
        serializer = OsobaModelSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        osoba = self.get_object(pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def osoba_add(request):
    if request.method == 'POST':
        serializer = OsobaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def osoba_list_zawiera(request, search_string):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(imie__icontains=search_string)
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def stanowisko_list(request):
    """
    Lista wszystkich obiektów modelu Stanowisko
    """
    if request.method == 'GET':
        st = Stanowisko.objects.all()
        serializer = StanowiskoModelSerializer(st, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StanowiskoModelSerializer(stanowisko)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StanowiskoModelSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
