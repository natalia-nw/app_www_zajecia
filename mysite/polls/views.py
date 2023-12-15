from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer

from django.core.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework import permissions
from django.core.exceptions import PermissionDenied
from .permissions import CustomDjangoModelPermissions
import copy


class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_list(request):

    if request.method == 'GET':
        persons = Osoba.objects.filter(wlasciciel=request.user)
        serializer = OsobaModelSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def osoba_detail(request, pk):

    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)


@api_view(['PUT', 'GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update(request, pk):

    osoba = get_object_or_404(Osoba, pk=pk)

    if osoba.wlasciciel != request.user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = OsobaModelSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk):

    osoba = get_object_or_404(Osoba, pk=pk)

    if osoba.wlasciciel != request.user:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)

    if request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_add(request):
    if request.method == 'POST':
        serializer = OsobaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([BearerTokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_stanowisko(request, id):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(stanowisko=id)
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def osoba_list_zawiera(request, search_string):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(imie__icontains=search_string)
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def stanowisko_list(request):
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


def osoba_view(request):
    if not request.user.has_perm('polls.view_osoba') or not request.user.has_perm('polls.can_view_other_persons'):
        return HttpResponse(f"Nie masz uprawnien view_osoba i can_view_other_persons.")
    osoby = Osoba.objects.all()
    message = ''
    for osoba in osoby:
        message += f'<br>{osoba}'
    return HttpResponse(f"Masz uprawnienia view_osoba i can_view_other_persons. <br>{message}")


class OsobaListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]

    def get_queryset(self):
        return Osoba.objects.all()

    def get(self, request):
        osoby = Osoba.objects.all()
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)
