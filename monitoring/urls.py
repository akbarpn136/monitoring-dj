from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^atribut/(?P<dt_frm>\d{4}-\d{2}-\d{2})/(?P<dt_to>\d{4}-\d{2}-\d{2})$', views.json_atr_angin,
        name='json_angin'),
    url(r'^rose/(?P<dt_frm>\d{4}-\d{2}-\d{2})/(?P<dt_to>\d{4}-\d{2}-\d{2})/'
        r'(?P<vmax>[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)/(?P<step>[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)/$',
        views.json_rose_angin,
        name='json_rose'),
    url(r'^pdf/(?P<dt_frm>\d{4}-\d{2}-\d{2})/(?P<dt_to>\d{4}-\d{2}-\d{2})$', views.json_pdf_angin,
        name='json_pdf'),
    url(r'^wtr/(?P<dt_frm>\d{4}-\d{2}-\d{2})/(?P<dt_to>\d{4}-\d{2}-\d{2})/'
        r'(?P<grup>[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)/(?P<step>[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)/'
        r'(?P<kompas>[\w]+)/$', views.json_wtr_angin, name='json_wtr'),

    url(r'^$', views.index, name='halaman_utama'),
    url(r'^(?P<pk>[0-9]+)/visual/$', views.visual, name='halaman_visual'),
]
