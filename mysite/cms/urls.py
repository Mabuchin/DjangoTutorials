#!/usr/bin/ python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns,url
from cms import views

urlpatterns = patterns('',

	url(r'^book/$', views.book_list, name='book_list'),
	url(r'^book/add/$', views.book_edit, name='book_add'),
	url(r'^book/mod/(?P<book_id>\d+)/$', views.book_edit, name = 'book_mod'),
	url(r'^book/del/(?P<book_id>\d+)/$', views.book_del, name = 'book_del'),

	url(r'^impression/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name = 'impression_list'),

	url(r'^impression/add/(?P<book_id>\d+)/$', views.ImpressionList.as_view(), name = 'impression_add'),

	url(r'^impression/edit/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.ImpressionList.as_view(), name = 'impression_mod'),

	url(r'^impression/del/(?P<book_id>\d+)/(?P<impression_id>\d+)/$', views.ImpressionList.as_view(), name = 'impression_del'),
	)