from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/atribut/$', views.json_atr_angin, name='json_angin'),

    url(r'^$', views.index, name='halaman_utama'),
    url(r'^(?P<pk>[0-9]+)/$', views.index, name='halaman_utama_pk'),
    url(r'^(?P<pk>[0-9]+)/visual/(?P<daerah>[0-9]+)/daerah/$', views.visual, name='halaman_visual'),
]
