# Generated by Django 3.1.4 on 2020-12-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_jop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
