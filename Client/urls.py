from django.contrib import admin
from django.urls import path
from .views import HomePage, AddPageView, ClientListView , DeletePageView , export, upload
from . import views
from django.conf.urls import url


urlpatterns = [
    path('' , views.HomePage , name = 'HomePage'),
    path('AddPage/' , views.AddPageView , name = 'AddPage'),
    path('ClientList/' , views.ClientListView.as_view() , name = 'ClientList'),
    path('<int:pk>/DeletePage/' , views.DeletePageView.as_view() , name = 'Delete'),
    path('<int:pk>/UpdatePage/' , views.UpdatePageView.as_view() , name = 'Update'),
    url(r'^export-xlsx/$', views.export, name='export'),
    path('import/' , views.upload , name = 'import'),

]