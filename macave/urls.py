from django.conf.urls import url, patterns


urlpatterns = patterns('macave.views',
    url(r'^$', 'cave', name='cave'),
    url(r'^liste_vins/', 'vins', name='vins'),
    url(r'^vin_detail/(?P<pk>[0-9]+)/$', 'vin_detail', name='vin_detail'),
                       )
