# -*- coding: utf-8 -*-
from django.db  import models
from django.urls import reverse

class Clients(models.Model):
    nom= models.CharField(max_length=20)

    prenom= models.CharField(max_length=20)

    email= models.EmailField()

    telephone= models.CharField(max_length=15)

    date_souscription= models.DateField()
    
    situation= models.BooleanField(default= True)

    class Meta:
        db_table = "web_member"

    def __str__(self):
        return f'{self.nom} {self.prenom}'

    def get_absolute_url(self):
        return reverse('clients-detail' , args= [str(self.id)])