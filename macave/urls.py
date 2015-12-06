from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'macave.views.accueil', name='accueil'),
    url(r'^vins/', 'macave.views.vins', name='vins'),
    url(r'^vin/(?P<pk>[0-9]+)/$', 'macave.views.vin_detail', name='post_detail'),

]
