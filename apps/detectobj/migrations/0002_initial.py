# Generated by Django 3.2.12 on 2022-08-04 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detectobj', '0001_initial'),
        ('modelmanager', '0001_initial'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedetection',
            name='detectionmodel',
            field=models.ForeignKey(help_text='Model used for detection', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='detectedimages', to='modelmanager.mlmodel'),
        ),
        migrations.AddField(
            model_name='imagedetection',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Main Image', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detectedimages', to='images.imagefile'),
        ),
    ]
