# Generated by Django 2.1 on 2018-10-16 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signals', '0021_auto_20181016_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'created_at',
                    models.DateTimeField(auto_now_add=True)
                ),
                (
                    'updated_at',
                    models.DateTimeField(auto_now=True)
                ),
                (
                    'text',
                    models.TextField(max_length=3000)
                ),
                (
                    'created_by',
                    models.EmailField(blank=True, max_length=254, null=True)
                ),
                (
                    '_signal',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='notes',
                        to='signals.Signal'
                    )
                )
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
