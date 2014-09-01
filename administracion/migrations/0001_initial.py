# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recurso'
        db.create_table(u'administracion_recurso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'administracion', ['Recurso'])

        # Adding model 'Ejercicio'
        db.create_table(u'administracion_ejercicio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('solucion', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('dificultad', self.gf('django.db.models.fields.CharField')(default='normal', max_length=10, null=True)),
            ('edad_minima', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
            ('edad_maxima', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'administracion', ['Ejercicio'])

        # Adding M2M table for field recursos on 'Ejercicio'
        m2m_table_name = db.shorten_name(u'administracion_ejercicio_recursos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ejercicio', models.ForeignKey(orm[u'administracion.ejercicio'], null=False)),
            ('recurso', models.ForeignKey(orm[u'administracion.recurso'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ejercicio_id', 'recurso_id'])

        # Adding model 'Actividad'
        db.create_table(u'administracion_actividad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'administracion', ['Actividad'])

        # Adding M2M table for field ejercicios on 'Actividad'
        m2m_table_name = db.shorten_name(u'administracion_actividad_ejercicios')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividad', models.ForeignKey(orm[u'administracion.actividad'], null=False)),
            ('ejercicio', models.ForeignKey(orm[u'administracion.ejercicio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['actividad_id', 'ejercicio_id'])

        # Adding model 'Jugador'
        db.create_table(u'administracion_jugador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identificador', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'administracion', ['Jugador'])

        # Adding model 'Refugio'
        db.create_table(u'administracion_refugio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('localizacion', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'administracion', ['Refugio'])

        # Adding M2M table for field actividades on 'Refugio'
        m2m_table_name = db.shorten_name(u'administracion_refugio_actividades')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('refugio', models.ForeignKey(orm[u'administracion.refugio'], null=False)),
            ('actividad', models.ForeignKey(orm[u'administracion.actividad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['refugio_id', 'actividad_id'])

        # Adding model 'Sesion'
        db.create_table(u'administracion_sesion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jugador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administracion.Jugador'])),
            ('refugio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administracion.Refugio'])),
            ('inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('fin', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal(u'administracion', ['Sesion'])

        # Adding model 'Resultado'
        db.create_table(u'administracion_resultado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sesion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administracion.Sesion'])),
            ('actividad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administracion.Actividad'])),
            ('ejercicio', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['administracion.Ejercicio'])),
            ('respuesta', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'administracion', ['Resultado'])


    def backwards(self, orm):
        # Deleting model 'Recurso'
        db.delete_table(u'administracion_recurso')

        # Deleting model 'Ejercicio'
        db.delete_table(u'administracion_ejercicio')

        # Removing M2M table for field recursos on 'Ejercicio'
        db.delete_table(db.shorten_name(u'administracion_ejercicio_recursos'))

        # Deleting model 'Actividad'
        db.delete_table(u'administracion_actividad')

        # Removing M2M table for field ejercicios on 'Actividad'
        db.delete_table(db.shorten_name(u'administracion_actividad_ejercicios'))

        # Deleting model 'Jugador'
        db.delete_table(u'administracion_jugador')

        # Deleting model 'Refugio'
        db.delete_table(u'administracion_refugio')

        # Removing M2M table for field actividades on 'Refugio'
        db.delete_table(db.shorten_name(u'administracion_refugio_actividades'))

        # Deleting model 'Sesion'
        db.delete_table(u'administracion_sesion')

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
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['administracion.Recurso']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'solucion': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
            'ejercicio': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['administracion.Ejercicio']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sesion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administracion.Sesion']"})
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