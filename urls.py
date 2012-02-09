from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'verkefni3.views.home', name='home'),
    # url(r'^verkefni3/', include('verkefni3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^course/$', 'weschool.views.index'),
    url(r'^course/(?P<course_id>\d+)/$', 'weschool.views.detail'),
    url(r'^course/exam/(?P<exam_id>\d+)/$', 'weschool.views.action'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
