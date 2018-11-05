from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.tag_list, name='tag_list'),
    url(r'^question/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^ask/$', views.post_new, name='ask'),
    url(r'^hot/$', views.post_hot, name	='post_hot'),
    url(r'^tag/(?P<tag>)/$', views.post_tag, name='post_tag'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^settings/$', views.settings, name='settings'),
]
