from django.contrib import admin

from .models import Cliente, Pais, Instrumentos 

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Pais)
admin.site.register(Instrumentos)

