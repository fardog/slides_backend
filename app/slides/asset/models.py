from django.db import models

# Create your models here.
class AssetType(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = models.SlugField(max_length=15, blank=False, null=False)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.slug)

class Asset(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    path = models.FileField(upload_to='media')

    asset_type = models.ForeignKey(AssetType, blank=False, null=False)

    def __unicode__(self):
        return u'%s' % (self.name)
