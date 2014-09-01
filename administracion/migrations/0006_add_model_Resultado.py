# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resultado'
        db.create_table(u'administracion_resultado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actividad', self.gf('django.db.models.fields.PositiveIntegerField')(default=-1)),
            ('ejercicio', self.gf('django.db.models.fields.PositiveIntegerField')(default=-1)),
            ('tiempo_respuesta', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('respuesta', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'administracion', ['Resultado'])


    def backwards(self, orm):
        # Deleting model 'Resultado'
        db.delete_table(u'administracion_resultado')


    models = {
        u'administracion.actividad': {
            'Meta': {'object_name': 'Actividad'},
            'ejercicios': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['administracion.Ejercicio']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'administracion.ejercicio': {
            'Meta': {'object_name': 'Ejercicio'},
            'dificultad': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '10', 'null': 'True'}),
            'edad_maxima': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'edad_minima': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['administracion.Recurso']", 'null': 'True', 'blank': 'True'}),
            'solucion': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tipo': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'tipo_respuesta': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'administracion.jugador': {
            'Meta': {'object_name': 'Jugador'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identificador': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'administracion.recurso': {
            'Meta': {'object_name': 'Recurso'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'administracion.refugio': {
            'Meta': {'object_name': 'Refugio'},
            'actividades': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['administracion.Actividad']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localizacion': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'administracion.resultado': {
            'Meta': {'object_name': 'Resultado'},
            'actividad': ('django.db.models.fields.PositiveIntegerField', [], {'default': '-1'}),
            'ejercicio': ('django.db.models.fields.PositiveIntegerField', [], {'default': '-1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tiempo_respuesta': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'administracion.sesion': {
            'Meta': {'object_name': 'Sesion'},
            'fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'jugador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administracion.Jugador']"}),
            'refugio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administracion.Refugio']"})
        }
    }

    complete_apps = ['administracion']