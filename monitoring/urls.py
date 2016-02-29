from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/atribut/(?P<dt_frm>\d{4}-\d{2}-\d{2})/(?P<dt_to>\d{4}-\d{2}-\d{2})$', views.json_atr_angin,
        name='json_angin'),
    url(r'^(?P<pk>[0-9]+)/rose/(?P<dt_frm>\d{4}-\d{2}-\d{2})/(?P<dt_to>\d{4}-\d{2}-\d{2})$', views.json_rose_angin,
        name='json_rose'),
    url(r'^(?P<pk>[0-9]+)/pdf/(?P<dt_frm>\d{4}-\d{2}-\d{2})/(?P<dt_to>\d{4}-\d{2}-\d{2})$', views.json_pdf_angin,
        name='json_pdf'),
    url(r'^(?P<pk>[0-9]+)/pdf/(?P<dt_frm>\d{4}-\d{2}-\d{2})/(?P<dt_to>\d{4}-\d{2}-\d{2})$', views.json_wtr_angin,
        name='json_wtr'),

    url(r'^$', views.index, name='halaman_utama'),
    url(r'^(?P<pk>[0-9]+)/$', views.index, name='halaman_utama_pk'),
    url(r'^(?P<pk>[0-9]+)/visual/(?P<daerah>[0-9]+)/daerah/$', views.visual, name='halaman_visual'),
]
