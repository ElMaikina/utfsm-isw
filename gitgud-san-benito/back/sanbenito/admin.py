from django.contrib import admin

# Register your models here.
from .models import Carabinero
from .models import Inspector
from .models import Infraccion

admin.site.register(Carabinero)
admin.site.register(Inspector)
admin.site.register(Infraccion)
