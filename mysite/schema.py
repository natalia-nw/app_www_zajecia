import graphene
from graphene_django import DjangoObjectType

from polls.models import Person, Team, Stanowisko, Osoba


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("id", "name", "shirt_size", "month_added", "team")


class TeamType(DjangoObjectType):
    class Meta:
        model = Team
        fields = ("id", "name", "country")


class OsobaType(DjangoObjectType):
    class Meta:
        model = Osoba
        fields = ("id", "imie", "nazwisko", "plec", "stanowisko", "data_dodania", "wlasciciel")


class StanowiskoType(DjangoObjectType):
    class Meta:
        model = Stanowisko
        fields = ("id", "nazwa", "opis")


class Query(graphene.ObjectType):
    all_teams = graphene.List(TeamType)
    person_by_id = graphene.Field(PersonType, id=graphene.Int(required=True))
    all_persons = graphene.List(PersonType)
    person_by_name = graphene.Field(PersonType, name=graphene.String(required=True))
    find_persons_name_by_phrase = graphene.List(PersonType, substr=graphene.String(required=True))

    find_stanowiskos_nazwa_by_phrase = graphene.List(StanowiskoType, substr=graphene.String(required=True))
    osobas_of_wlasciciel = graphene.List(OsobaType, id=graphene.Int())
    find_osobas_imie_by_phrase = graphene.List(OsobaType, substr=graphene.String(required=True))

    def resolve_all_teams(root, info):
        return Team.objects.all()

    def resolve_person_by_id(root, info, id):
        try:
            return Person.objects.get(pk=id)
        except Person.DoesNotExist:
            raise Exception('Invalid person Id')

    def resolve_person_by_name(root, info, name):
        try:
            return Person.objects.get(name=name)
        except Person.DoesNotExist:
            raise Exception(f'No Person with name \'{name}\' found.')

    def resolve_all_persons(root, info):
        """ zwraca również wszystkie powiązane obiekty team dla tego obiektu Person"""
        return Person.objects.select_related("team").all()

    def resolve_find_persons_name_by_phrase(self, info, substr):
        return Person.objects.filter(name__icontains=substr)

    # zadanie
    def resolve_find_stanowiskos_nazwa_by_phrase(self, info, substr):
        return Stanowisko.objects.filter(nazwa__icontains=substr)

    def resolve_osobas_of_wlasciciel(self, info, id):
        return Osoba.objects.filter(wlasciciel__id=id)

    def resolve_find_osobas_imie_by_phrase(self, info, substr):
        return Osoba.objects.filter(imie__icontains=substr)


schema = graphene.Schema(query=Query)

