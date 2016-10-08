from django.conf.urls import url
from . import views

urlpatterns = [
    #widok post_list do pustego URL
    url(r'^$', views.post_list, name='post_list'),
]
