from django.db import models

from slides.asset.models import Asset



class Presentation(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = models.SlugField(max_length=15, blank=False, null=False)

    assets = models.ManyToManyField(Asset, through='PresentationAsset')

    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class PresentationAsset(models.Model):
    presentation = models.ForeignKey(Presentation)
    asset = models.ForeignKey(Asset)

    order = models.IntegerField(default=0, blank=False, null=False)
    time = models.FloatField(default=5.0, blank=False, null=False)

    class Meta:
        ordering = ["order"]

