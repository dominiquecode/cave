from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'blog.views.accueil', name='accueil'),
    url(r'^articles/', 'blog.views.articles', name='articles'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^post/new/$', 'blog.views.post_new', name='post_new'),
]
