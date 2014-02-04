# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Asset.last_modified'
        db.add_column(u'asset_asset', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 2, 4, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Asset.last_modified'
        db.delete_column(u'asset_asset', 'last_modified')


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
        }
    }

    complete_apps = ['asset']