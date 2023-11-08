from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Carabinero
from .models import Inspector
from .models import Infractor
from .models import Juez
from .models import Infraccion
from .models import AppUserManager
from .models import AppUser


admin.site.register(Carabinero)
admin.site.register(Inspector)
admin.site.register(Infractor)
admin.site.register(Juez)
admin.site.register(Infraccion)
admin.site.register(AppUserManager)
admin.site.register(AppUser)
