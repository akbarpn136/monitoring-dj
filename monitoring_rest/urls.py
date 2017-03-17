from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^angin/(?P<date_from>\d{4}-\d{2}-\d{2})/(?P<date_to>\d{4}-\d{2}-\d{2})/$',
        views.MonitorAngin.as_view(),
        name='atribut_angin'),
    url(r'^windrose/(?P<date_from>\d{4}-\d{2}-\d{2})/(?P<date_to>\d{4}-\d{2}-\d{2})/',
        views.MonitorWindrose.as_view(),
        name='windrose_angin'),
]
