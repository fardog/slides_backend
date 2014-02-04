from django.db import models

from slides.presentation.models import Presentation

class Display(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    slug = models.SlugField(max_length=30, blank=False, null=False)

    presentation = models.ForeignKey(Presentation, blank=False, null=False)

    def __unicode__(self):
        return u'%s' % (self.name)
