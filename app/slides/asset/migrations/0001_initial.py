# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AssetType'
        db.create_table(u'asset_assettype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=15)),
        ))
        db.send_create_signal(u'asset', ['AssetType'])

        # Adding model 'Asset'
        db.create_table(u'asset_asset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('path', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('asset_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['asset.AssetType'])),
        ))
        db.send_create_signal(u'asset', ['Asset'])


    def backwards(self, orm):
        # Deleting model 'AssetType'
        db.delete_table(u'asset_assettype')

        # Deleting model 'Asset'
        db.delete_table(u'asset_asset')


    models = {
        u'asset.asset': {
            'Meta': {'object_name': 'Asset'},
            'asset_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['asset.AssetType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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