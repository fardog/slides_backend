from tastypie import fields
from tastypie.resources import ModelResource
from string import upper
from django.http import HttpResponse
from tastypie.exceptions import ImmediateHttpResponse

from .presentation.models import Presentation, PresentationAsset
from .asset.models import Asset

# https://gist.github.com/robhudson/3848832
class CORSResource(object):
    """
    Adds CORS headers to resources that subclass this.
    """
    def create_response(self, *args, **kwargs):
        response = super(CORSResource, self).create_response(*args, **kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    def method_check(self, request, allowed=None):
        if allowed is None:
            allowed = []

        request_method = request.method.lower()
        allows = ','.join(map(upper, allowed))

        if request_method == 'options':
            response = HttpResponse(allows)
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Headers'] = 'Content-Type'
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        if not request_method in allowed:
            response = http.HttpMethodNotAllowed(allows)
            response['Allow'] = allows
            raise ImmediateHttpResponse(response=response)

        return request_method

# http://stackoverflow.com/questions/10629047/django-tastypie-and-many-to-many-through-relationships
# http://eugene-yeo.me/2012/12/4/django-tastypie-manytomany-through-part-2/
class AssetResource(CORSResource, ModelResource):
    class Meta:
        queryset = Asset.objects.all()
        resource_name = 'assets'

class PresentationAssetResource(CORSResource, ModelResource):
    asset = fields.ToOneField(AssetResource, 'asset', full=True)

    class Meta:
        queryset = PresentationAsset.objects.all()

class PresentationResource(CORSResource, ModelResource):
    assets = fields.ToManyField(PresentationAssetResource,
        attribute=lambda bundle: bundle.obj.assets.through.objects.filter(
            presentation=bundle.obj) or bundle.obj.assets, full=True)

    class Meta:
        queryset = Presentation.objects.all()
        resource_name = 'presentation'
