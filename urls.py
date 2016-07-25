# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import apps.entry
urlpatterns = patterns('apps.entry.views',
  url(r'^$','entry'),#這樣做似乎是對應到首頁
)