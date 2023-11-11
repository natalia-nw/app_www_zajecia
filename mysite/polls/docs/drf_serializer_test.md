Team
>>> from polls.models import Team
>>> from polls.serializers import TeamSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> team = Team(name='Bears', country='UK')
>>> team.save()
>>> serializer = TeamSerializer(team)
>>> serializer.data
{'id': 2, 'name': 'Bears', 'country': 'UK'}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":2,"name":"Bears","country":"UK"}'
>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> desrializer = TeamSerializer(data=data)
>>> desrializer.is_valid()
True
>>> desrializer.errors
{}
>>> desrializer.fields
{'id': IntegerField(read_only=True), 'name': CharField(required=True), 'country': CharField(required=True)}
>>> repr(desrializer)
"TeamSerializer(data={'id': 2, 'name': 'Bears', 'country': 'UK'}):\n    id = IntegerField(read_only=True)\n    name = Char
Field(required=True)\n    country = CharField(required=True)"
>>> desrializer.validated_data
OrderedDict([('name', 'Bears'), ('country', 'UK')])
>>> desrializer.save()
<Team: Bears>
>>> desrializer.data
{'id': 3, 'name': 'Bears', 'country': 'UK'}


Osoba
>>> from polls.models import Osoba
>>> from polls.serializers import OsobaModelSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> osoba = Osoba(imie='Bartosz', nazwisko='Testowy', plec='2', data_dodania='2023-10-10')
>>> osoba.save()
>>> serializer = OsobaModelSerializer(osoba)
>>> serializer.data
{'id': 7, 'imie': 'Bartosz', 'nazwisko': 'Testowy', 'plec': 2, 'stanowisko': None, 'data_dodania': '2023-10-10'}
>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":7,"imie":"Bartosz","nazwisko":"Testowy","plec":2,"stanowisko":null,"data_dodania":"2023-10-10"}'
>>> import io
>>> stream = io.BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> deserializer = OsobaModelSerializer(data=data)
>>> deserializer.is_valid()
True
>>> deserializer.errors
{}
>>> deserializer.fields
{'id': IntegerField(label='ID', read_only=True), 'imie': CharField(max_length=30), 'nazwisko': CharField(max_length=30), '
plec': ChoiceField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inne')]), 'stanowisko': PrimaryKeyRelatedField(allow_nu
ll=True, queryset=Stanowisko.objects.all(), required=False), 'data_dodania': DateField()}
>>> repr(deserializer)
"OsobaModelSerializer(data={'id': 7, 'imie': 'Bartosz', 'nazwisko': 'Testowy', 'plec': 2, 'stanowisko': None, 'data_dodani
a': '2023-10-10'}):\n    id = IntegerField(label='ID', read_only=True)\n    imie = CharField(max_length=30)\n    nazwisko
= CharField(max_length=30)\n    plec = ChoiceField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inne')])\n    stanowisk
o = PrimaryKeyRelatedField(allow_null=True, queryset=Stanowisko.objects.all(), required=False)\n    data_dodania = DateFie
ld()"
>>> deserializer.validated_data
OrderedDict([('imie', 'Bartosz'), ('nazwisko', 'Testowy'), ('plec', 2), ('stanowisko', None), ('data_dodania', datetime.da
te(2023, 10, 10))])
>>> deserializer.save()
<Osoba: Bartosz Testowy>
>>> deserializer.data
{'id': 8, 'imie': 'Bartosz', 'nazwisko': 'Testowy', 'plec': 2, 'stanowisko': None, 'data_dodania': '2023-10-10'}
>>>
