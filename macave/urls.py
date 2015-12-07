from django.conf.urls import url, patterns


urlpatterns = patterns('macave.views',
    url(r'^$', 'accueil', name='accueil'),
    url(r'^vins/', 'vins', name='vins'),
    url(r'^vin/(?P<pk>[0-9]+)/$', 'vin_detail', name='vin_detail'),
                       )
