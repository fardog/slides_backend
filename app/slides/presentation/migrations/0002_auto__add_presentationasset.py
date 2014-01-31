# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PresentationAsset'
        db.create_table(u'presentation_presentationasset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('presentation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['presentation.Presentation'])),
            ('asset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['asset.Asset'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('time', self.gf('django.db.models.fields.FloatField')(default=5.0)),
        ))
        db.send_create_signal(u'presentation', ['PresentationAsset'])

        # Removing M2M table for field assets on 'Presentation'
        db.delete_table(db.shorten_name(u'presentation_presentation_assets'))


    def backwards(self, orm):
        # Deleting model 'PresentationAsset'
        db.delete_table(u'presentation_presentationasset')

        # Adding M2M table for field assets on 'Presentation'
        m2m_table_name = db.shorten_name(u'presentation_presentation_assets')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('presentation', models.ForeignKey(orm[u'presentation.presentation'], null=False)),
            ('asset', models.ForeignKey(orm[u'asset.asset'], null=False))
        ))
        db.create_unique(m2m_table_name, ['presentation_id', 'asset_id'])


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
        },
        u'presentation.presentation': {
            'Meta': {'object_name': 'Presentation'},
            'assets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['asset.Asset']", 'through': u"orm['presentation.PresentationAsset']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '15'})
        },
        u'presentation.presentationasset': {
            'Meta': {'object_name': 'PresentationAsset'},
            'asset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['asset.Asset']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'presentation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['presentation.Presentation']"}),
            'time': ('django.db.models.fields.FloatField', [], {'default': '5.0'})
        }
    }

    complete_apps = ['presentation']