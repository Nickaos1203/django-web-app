# Generated by Django 5.0.6 on 2024-05-11 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_annonce_remove_band_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Annonce',
        ),
        migrations.AddField(
            model_name='band',
            name='title',
            field=models.CharField(default='None', max_length=150),
        ),
    ]
