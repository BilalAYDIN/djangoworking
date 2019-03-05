from django.conf.urls import url
from .views import *


app_name= 'post'

urlpatterns = [


    url(r'^index/$', post_index, name='index'),
    url(r'^indexy/$', post_indexy, name='indexy'),
    url(r'^indexsat/$', post_indexsat, name='indexsat'),
    url(r'^indexsatrapor/$', post_indexsatrapor, name='indexsatrapor'), # rapor için gerekli
    url(r'^indexhurda/$', post_indexhurda, name='indexhurda'),
    url(r'^indexemanet/$', post_indexemanet, name='indexemanet'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/updatedate/$', post_updatedate, name='updatedate'),
    url(r'^(?P<slug>[\w-]+)/updateiade/$', post_updateiade, name='updateiade'),
    url(r'^(?P<slug>[\w-]+)/updateiadesat/$', post_updateiadesat, name='updateiadesat'),
    url(r'^(?P<slug>[\w-]+)/updateiadeem/$', post_updateiadeem, name='updateiadeem'),
    url(r'^(?P<slug>[\w-]+)/updateiadehu/$', post_updateiadehu, name='updateiadehu'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),
    url(r'^(?P<slug>[\w-]+)/deletex/$', post_deletex, name='deletex'),
    url(r'^(?P<slug>[\w-]+)/deletec/$', post_deletec, name='deletec'),

]


