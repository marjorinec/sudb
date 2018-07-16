# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-07 14:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('superuber', '0004_auto_20180707_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='pfpj',
            field=models.CharField(choices=[('PF', 'Pessoa f\xedsica'), ('PJ', 'Pessoa jur\xeddica')], default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pfpj',
            field=models.CharField(choices=[('PF', 'Pessoa f\xedsica'), ('PJ', 'Pessoa jur\xeddica')], default='PF', max_length=2),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='pfpj',
            field=models.CharField(choices=[('PF', 'Pessoa f\xedsica'), ('PJ', 'Pessoa jur\xeddica')], max_length=2),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='superuber.Cargo'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='departamento',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='superuber.Departamento'),
        ),
    ]