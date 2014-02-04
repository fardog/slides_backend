from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from slides.api import PresentationResource, AssetResource, DisplayResource

v1_api = Api(api_name='v1')
v1_api.register(PresentationResource())
v1_api.register(AssetResource())
v1_api.register(DisplayResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'slides.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)

# if we're debugging, serve up static files
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
