# Generated by Django 5.0.6 on 2024-05-11 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_band_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='band',
            name='title',
        ),
    ]
