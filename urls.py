from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #url(r'^login/$', 'django.contrib.auth.views.login'),
    # Examples:
    # url(r'^$', 'verkefni3.views.home', name='home'),
    # url(r'^verkefni3/', include('verkefni3.foo.urls')),
    url(r'^$', 'weschool.views.home_index' ),
    url(r'^login/$',  login),
    url(r'^logout/$', logout),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^course/$', 'weschool.views.index'),
    url(r'^course/(?P<course_id>\d+)/$', 'weschool.views.detail'),
    url(r'^course/exam/(?P<exam_id>\d+)/$', 'weschool.views.action'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
