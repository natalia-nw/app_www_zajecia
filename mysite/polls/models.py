import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# static choices
MONTHS = models.IntegerChoices('Miesiace',
                               'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

ANSWER = models.IntegerChoices('How are you?',
                               'Fine Excellent Good Surviving Idk')


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=60)
    whats_up = models.IntegerField(choices=ANSWER.choices, default=ANSWER.choices[0][0])

    def __str__(self):
        return f"{self.name}"


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=30)
    opis = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.nazwa}"


class Osoba(models.Model):

    class Plec(models.IntegerChoices):
        KOBIETA = 1
        MĘŻCZYZNA = 2
        INNE = 3

    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    plec = models.IntegerField(choices=Plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateField('data dodania')

    class Meta:
        ordering = ["nazwisko"]

    def __str__(self):
        return '%s %s' % (self.imie, self.nazwisko)

    def was_published_recently(self):
        return self.data_dodania >= datetime.today()
