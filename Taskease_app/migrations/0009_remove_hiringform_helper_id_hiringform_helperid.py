# Generated by Django 5.1.1 on 2024-10-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskease_app', '0008_remove_hiringform_helper_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hiringform',
            name='helper_id',
        ),
        migrations.AddField(
            model_name='hiringform',
            name='helperid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
