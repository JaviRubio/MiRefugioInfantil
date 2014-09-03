# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Resultado.sesion'
        db.add_column(u'administracion_resultado', 'sesion',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['administracion.Sesion']),
                      keep_default=False)

        # Deleting field 'Sesion.resultados'
        db.delete_column(u'administracion_sesion', 'resultados_id')


    def backwards(self, orm):
        # Deleting field 'Resultado.sesion'
        db.delete_column(u'administracion_resultado', 'sesion_id')

        # Adding field 'Sesion.resultados'
        db.add_column(u'administracion_sesion', 'resultados',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administracion.Resultado'], null=True),
                      keep_default=False)


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
            'actividad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administracion.Actividad']"}),
            'ejercicio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administracion.Ejercicio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sesion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administracion.Sesion']"}),
            'tiempo_respuesta': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'administracion.sesion': {
            'Meta': {'object_name': 'Sesion'},
            'fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'jugador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administracion.Jugador']"}),
            'refugio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administracion.Refugio']"})
        }
    }

    complete_apps = ['administracion']