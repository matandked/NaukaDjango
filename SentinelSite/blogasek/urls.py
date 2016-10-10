from django.conf.urls import url
from . import views

urlpatterns = [
    #widok post_list do pustego URL
    url(r'^$', views.post_list, name='post_list'),
    # /post/numer przezkaze numer do <pk> i wysle do post_detail
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
