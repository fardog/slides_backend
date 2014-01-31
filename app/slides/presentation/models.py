from django.db import models

from slides.asset.models import Asset

# Create your models here.
class Presentation(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = models.SlugField(max_length=15, blank=False, null=False)

    assets = models.ManyToManyField(Asset)

    def __unicode__(self):
        return u'%s' % (self.name)
