# Generated by Django 4.2.6 on 2023-10-24 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/notes'),
        ),
    ]
