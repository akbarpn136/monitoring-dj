from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='halaman_utama'),
    url(r'^(?P<pk>[0-9]+)/$', views.index, name='halaman_utama_pk'),
    url(r'^(?P<pk>[0-9]+)/visual/$', views.visual, name='halaman_visual'),
]
