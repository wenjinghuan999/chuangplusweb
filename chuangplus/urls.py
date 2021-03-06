from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from app.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chuangplus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
    url(r'^admin/', include(admin.site.urls)),
	
    # login
    url(r'^login/$', 'app.user.user_login'),
    # logout
    url(r'^logout/$', 'app.user.user_logout'),

    # financing
    url(r'^financing/$', financing),
    # policy
    url(r'^policy/$', policy),
    # community
    url(r'^community/$', community),
    # about
    url(r'^about/$', about),
    # contract
    url(r'^contract/$', contract),
    # feedback
    url(r'^feedback/$', feedback),
	
	# index-investor
    url(r'^inv/$', 'app.views.index_inv'),
	# index
    url(r'^$', 'app.views.index'),
	
)
