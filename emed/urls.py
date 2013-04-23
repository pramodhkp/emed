from django.conf.urls.defaults import patterns, include, url
from diagnosis.views import DiagnosisView
from django.conf import settings



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^assets/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),    
    # url(r'^about/$', AboutView.as_view(template_name="base.html"),
    		 # name='about'),    
    # url(r'^contact/$', ContactView.as_view(template_name="contact.html"),
    		 # name='contact'),
    url(r'^diagnosis/$', DiagnosisView.as_view(),
    		 name='diagnosis'),

    url(r'^admin/', include(admin.site.urls)),
)
