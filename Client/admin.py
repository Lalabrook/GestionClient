from django.contrib import admin
from .models import Clients
from import_export.admin import ImportExportModelAdmin

@admin.register(Clients)
class ClientAdmin(ImportExportModelAdmin):
    list_display = ('nom', 'prenom','email','telephone','date_souscription', 'situation')
    pass
