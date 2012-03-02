from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name='home'),
    url(r'^tweet/(?P<pk>\d+)$', 'main.views.tweet', name='tweet'),
    url(r'^tweet/(?P<pk>\d+)/edit$', 'main.views.edit_tweet', name='edit_tweet'),
    url(r'^zombie/(?P<pk>\d+)/edit$', 'main.views.edit_zombie', name='edit_zombie'),
    url(r'^tweet/(?P<pk>\d+)/delete$', 'main.views.delete_tweet', name='delete_tweet'),
    url(r'^zombie/(?P<pk>\d+)/delete$', 'main.views.delete_zombie', name='delete_zombie'),
    url(r'^tweet/new/$', 'main.views.new_tweet', name='new_tweet' ),
    url(r'^zombie/new/$', 'main.views.new_zombie', name='new_zombie' ),

)
