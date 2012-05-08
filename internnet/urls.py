from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('internapp.views',
    # Examples:
    # url(r'^$', 'internnet.views.home', name='home'),
    # url(r'^internnet/', include('internnet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    
    url(r'^$', 'index'),
    url(r'^jobs/(?P<job_id>\d+)/$', 'detail', name='job_detail'),
    url(r'^jobs/(?P<job_id>\d+)/review/$', 'review'),
    url(r'^company/(?P<company_id>\d+)/$', 'company'),
    url(r'^admin/', include(admin.site.urls)),
    
)
