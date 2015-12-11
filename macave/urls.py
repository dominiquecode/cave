from django.conf.urls import url, patterns


urlpatterns = patterns('macave.views',
    url(r'^$', 'cave', name='cave'),
    url(r'^liste_vins/', 'liste_vins', name='liste_vins'),
    url(r'^vin_detail/(?P<pk>[0-9]+)/$', 'vin_detail', name='vin_detail'),
    url(r'^unverre$', 'unverre', name='unverre'),
    url(r'^informations', 'informations', name='informations'),
                       )
