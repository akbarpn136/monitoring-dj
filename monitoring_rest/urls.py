from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^token_auth/$', views.GetToken.as_view(), name='auth_token'),
    url(r'^token_check/(?P<token>\w+)/$', views.CheckToken.as_view(), name='cek_token'),
    url(r'^rms/$', views.MonitorRMS.as_view(), name='rms_angin'),
    url(r'^angin/(?P<date_from>\d{4}-\d{2}-\d{2})/(?P<date_to>\d{4}-\d{2}-\d{2})/$',
        views.MonitorAngin.as_view(),
        name='atribut_angin'),
    url(r'^windrose/(?P<date_from>\d{4}-\d{2}-\d{2})/(?P<date_to>\d{4}-\d{2}-\d{2})/$',
        views.MonitorWindrose.as_view(),
        name='windrose_angin'),
    url(r'^pdf/(?P<date_from>\d{4}-\d{2}-\d{2})/(?P<date_to>\d{4}-\d{2}-\d{2})/$',
        views.MonitorPdf.as_view(),
        name='pdf_angin'),
    url(r'^waterfall/(?P<date_from>\d{4}-\d{2}-\d{2})/(?P<date_to>\d{4}-\d{2}-\d{2})/$',
        views.MonitorWaterfall.as_view(),
        name='waterfall_angin'),
]
