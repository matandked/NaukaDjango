from django.shortcuts import render
from django.conf import settings

#tu sie odwolujemy do naszej logiki
from .models import ListaAplikacji

def lista_aplikacji(request):

#	{'zmienna_w_templejcie':zmiennaLokalnaieWyznaoczna}

    appki = ListaAplikacji.objects.all()
    return render(request, 'glowna/lista_aplikacji.html', {
		'aplikacje':settings.INSTALLED_APPS,
		'aplikacyjki':appki})
