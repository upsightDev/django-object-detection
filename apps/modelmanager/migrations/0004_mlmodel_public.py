# Generated by Django 3.2.12 on 2022-08-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelmanager', '0003_alter_mlmodel_class_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlmodel',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
