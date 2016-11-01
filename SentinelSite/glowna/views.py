from django.shortcuts import render

from django.conf import settings

def lista_aplikacji(request):
    return render(request, 'glowna/lista_aplikacji.html', {'aplikacje':settings.INSTALLED_APPS})
