from django.contrib import admin

from .models import Question
from .models import Team
from .models import Person
from .models import Test
from .models import Stanowisko
from .models import Osoba

admin.site.register(Question)
admin.site.register(Team)
# admin.site.register(Person)
admin.site.register(Test)
# admin.site.register(Stanowisko)
# admin.site.register(Osoba)


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'shirt_size']


admin.site.register(Person, PersonAdmin)


class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa']
    list_filter = ['nazwa']


admin.site.register(Stanowisko, StanowiskoAdmin)


class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'stanowisko_id', 'data_dodania']
    list_filter = ('stanowisko', 'data_dodania')

    @admin.display(description='stanowisko(id)')
    def stanowisko_id(self, obj):
        if obj.stanowisko is not None:
            return str(obj.stanowisko.nazwa) + " (" + str(obj.stanowisko.id) + ")"
        return "-"


admin.site.register(Osoba, OsobaAdmin)
