from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^post_url/$', views.post_snippet, name='post_snippet'),
]