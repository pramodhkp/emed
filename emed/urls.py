from django.conf.urls.defaults import patterns, include, url
from diagnosis.views import SymptomView, DiagnosisView, HomeView, AboutView, ContactView, SearchView, UnifSearchView


from django.conf import settings



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^assets/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }), 
    url(r'^$', HomeView.as_view(),
    		 name='home'),   
    url(r'^about/$', AboutView.as_view(template_name="about.html"),
    		 name='about'),    
    url(r'^contact/$', ContactView.as_view(template_name="contact.html"),
    		 name='contact'),
    url(r'^diagnosis/$', SymptomView.as_view(),
    		 name='diagnosis'),
    url(r'^search/$', SearchView.as_view(),
    		 name='search'),
    url(r'^searchform/$', UnifSearchView.as_view(),
    		 name='search-form'),
    url(r'^results/$', DiagnosisView.as_view(),
    		 name='results'),

    url(r'^admin/', include(admin.site.urls)),
)
