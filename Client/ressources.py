from import_export import resources
from .models import Clients

class ClientRessource(resources.ModelResource):
    class Meta:
        model = Clients