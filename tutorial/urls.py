from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from newsletter.views import ProfileUpdateView, ProfileDeleteView


urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', 'newsletter.views.Contact', name='contact'),
    url(r'^about/$', 'tutorial.views.About', name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/$', 'newsletter.views.Profile', name = 'profile' ),
    url(r'^profile/(?P<sno_id>[0-9]+)/$', 'newsletter.views.wall', name = 'wall'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^edit/(?P<pk>\d+)$', ProfileUpdateView, name='update'),
    url(r'^delete/(?P<pk>\d+)$', ProfileDeleteView, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)