# Generated by Django 2.1.3 on 2019-02-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_film_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
