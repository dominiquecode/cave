from django.conf.urls import url


urlpatterns = [
    url(r'^blog$', 'blog.views.accueil', name='blog'),
    url(r'^articles/', 'blog.views.articles', name='articles'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', 'blog.views.post_edit', name='post_edit'),
    url(r'^post/new/$', 'blog.views.post_new', name='post_new'),
]
