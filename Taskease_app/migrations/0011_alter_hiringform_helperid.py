# Generated by Django 5.1.1 on 2024-10-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskease_app', '0010_alter_hiringform_helperid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiringform',
            name='helperid',
            field=models.IntegerField(),
        ),
    ]
