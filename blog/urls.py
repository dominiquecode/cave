from django.conf.urls import url, patterns


urlpatterns = patterns('blog.views',
                       url(r'^$', 'accueil', name='blog'),
                       url(r'^articles/', 'post_list', name='post_list'),
                       url(r'^post/(?P<pk>[0-9]+)/$', 'post_detail', name='post_detail'),
                       url(r'^post/(?P<pk>[0-9]+)/edit/$', 'post_edit', name='post_edit'),
                       url(r'^post/(?P<pk>[0-9]+)/publish/$', 'post_publish', name='post_publish'),
                       url(r'^post/(?P<pk>[0-9]+)/remove/$', 'post_remove', name='post_remove'),
                       url(r'^post/(?P<pk>[0-9]+)/comment/$', 'add_comment_to_post', name='add_comment_to_post'),
                       url(r'^comment/(?P<pk>[0-9]+)/approve/$', 'comment_approve', name='comment_approve'),
                       url(r'^comment/(?P<pk>[0-9]+)/remove/$', 'comment_remove', name='comment_remove'),
                       url(r'^post/new/$', 'post_new', name='post_new'),
                       url(r'^post/drafts/$', 'post_draft_list', name='post_draft_list'),
                       )
