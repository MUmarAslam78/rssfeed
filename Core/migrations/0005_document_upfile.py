# Generated by Django 4.0.4 on 2022-05-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_alter_document_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='upFile',
            field=models.CharField(default='', max_length=500),
        ),
    ]
