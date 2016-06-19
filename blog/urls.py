from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^aspi/$', views.aspi_post_list, name='aspi_post_list'),
    url(r'^code/$', views.code_post_list, name='code_post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail,  name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^faq/new/$', views.faq_new, name='faq_new'),
    url(r'^faq/(?P<pk>\d+)/$', views.faq_edit, name='faq_edit'),
    url(r'^faq/$', views.faq_list, name='faq_list'),
]
