# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import entry
urlpatterns = patterns('entry.views',
  url(r'^$','entry', name='entry'),#這樣做似乎是對應到首頁
)