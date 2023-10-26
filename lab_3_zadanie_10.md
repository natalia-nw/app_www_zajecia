>>> from polls.models import Osoba
>>> Osoba.objects.all()
<QuerySet [<Osoba: Marta A>, <Osoba: Stanisław B>, <Osoba: Adam Bb>, <Osoba: Alex C>]>
>>> Osoba.objects.filter(id=3)
<QuerySet [<Osoba: Alex C>]>
>>> Osoba.objects.filter(imie__startswith='A')
<QuerySet [<Osoba: Adam Bb>, <Osoba: Alex C>]>
>>> Osoba.objects.order_by().values_list('stanowisko__nazwa',flat=True).distinct()
<QuerySet ['Trener', 'Programista', 'Analityk']>
>>> Osoba.objects.order_by('-stanowisko__nazwa').values_list('stanowisko__nazwa',flat=True)
<QuerySet ['Trener', 'Programista', 'Analityk', 'Analityk']>
>>> new = Osoba(imie='Anastazja',nazwisko='Aa',plec=Osoba.Plec.KOBIETA,stanowisko_id=2,data_dodania='2023-10-25')
>>> new.save()
>>> Osoba.objects.all()
<QuerySet [<Osoba: Marta A>, <Osoba: Anastazja Aa>, <Osoba: Stanisław B>, <Osoba: Adam Bb>, <Osoba: Alex C>]>
>>>
