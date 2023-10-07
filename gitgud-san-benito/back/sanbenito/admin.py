from django.contrib import admin

# Register your models here.
from .models import Carabinero
from .models import Inspectores
from .models import Infracciones

admin.site.register(Carabinero)
admin.site.register(Inspectores)
admin.site.register(Infracciones)
