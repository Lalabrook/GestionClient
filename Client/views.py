# -*- coding: utf-8 -*-
from django.shortcuts import render , redirect
from .models import Clients
from .forms import ClientAddForm
from django.views.generic import ListView , DeleteView , UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .ressources import ClientRessource
from tablib import Dataset
from django.contrib import messages


def HomePage(request):
    return render(request, "HomePage.html")

def AddPageView(request):
    if len(request.POST)>0:
        form = ClientAddForm(request.POST)
        if form.is_valid():
            form.save()
            success="Enregistré avec succès !"
            return render(request, "AddPage.html", {'success':success, 'form':form} )
        else:
            error = "les champs ne sont pas valides"
            return render(request, "AddPage.html", {'error': error, 'form':form})
    else:
        error = "Veuillez entrez les informations du client"
        form = ClientAddForm()
        return render(request, "AddPage.html", {'error': error, 'form':form})


class ClientListView(ListView):
    model = Clients

class DeletePageView(DeleteView):
    model = Clients
    success_url = reverse_lazy('ClientList')

class UpdatePageView(UpdateView):
    model= Clients
    fields=['nom', 'prenom','email','telephone','date_souscription', 'situation']
    template_name_suffix= '_update_form'
    success_url = reverse_lazy('ClientList')

def export(request):
    clients_ressource =  ClientRessource()
    dataset = clients_ressource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="ListeClients.csv"'

    return response


def upload(request):
    if request.method == 'POST':
        clients_ressource = ClientRessource()
        dataset= Dataset()
        new_client = request.FILES['myfile']

        if not new_client.name.endswith('xlsx'):
            messages.info(request, 'mauvais format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_client.read(),format='xlsx')
        for data in imported_data:
            value = Clients(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
            )
            value.save()
    
    return render(request, 'upload.html' )


    



