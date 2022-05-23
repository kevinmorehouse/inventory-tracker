# Generated by Django 4.0.4 on 2022-05-18 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='deletion_comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='is_deleted',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
