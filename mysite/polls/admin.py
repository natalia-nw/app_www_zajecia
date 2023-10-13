from django.contrib import admin

from .models import Question
from .models import Team
from .models import Person
from .models import Test

admin.site.register(Question)
admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Test)
