# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.apps import apps
from django.apps import AppConfig

#linijka poniżej jest bezużyteczna - zmienna aplikacje nigdzie nie jest przekazywana itp.
#aplikacje = settings.INSTALLED_APPS

#aplikacje = apps.get_app_configs()

class ListaAplikacji(models.Model):
    #konfigi = apps.get_app_configs()
    konfigi = apps.get_app_config('blogasek')
    nazwa = apps.get_app_config('admin').verbose_name
    
    def __str__(self):
       return self.konfigi[0].name 
