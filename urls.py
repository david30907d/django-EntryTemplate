# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from entry import views
urlpatterns = [
  url(r'^$', views.entry, name='entry'),#這樣做似乎是對應到首頁
]