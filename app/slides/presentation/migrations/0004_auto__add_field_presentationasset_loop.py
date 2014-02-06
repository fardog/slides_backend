# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PresentationAsset.loop'
        db.add_column(u'presentation_presentationasset', 'loop',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PresentationAsset.loop'
        db.delete_column(u'presentation_presentationasset', 'loop')


    models = {
        u'asset.asset': {
            'Meta': {'object_name': 'Asset'},
            'asset_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['asset.AssetType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'path': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'asset.assettype': {
            'Meta': {'object_name': 'AssetType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '15'})
        },
        u'presentation.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'assets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['asset.Asset']", 'through': u"orm['presentation.PresentationAsset']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '15'})
        },
        u'presentation.presentationasset': {
            'Meta': {'ordering': "['order']", 'object_name': 'PresentationAsset'},
            'asset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['asset.Asset']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['presentation.Presentation']"}),
            'time': ('django.db.models.fields.FloatField', [], {'default': '7.0'})
        }
    }

    complete_apps = ['presentation']