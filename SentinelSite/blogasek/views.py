from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    #pobieramy posty jako QuerySet (to takie obiekty zassane z bazy danych)
    #Post zdefiniowalismy w modelach
    posty = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogasek/post_list.html', {'posts':posty})
    