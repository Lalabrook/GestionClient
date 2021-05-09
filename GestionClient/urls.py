# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path , include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('' , RedirectView.as_view(url = '/HomePage', permanent = True)),
    path('', include('Client.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

