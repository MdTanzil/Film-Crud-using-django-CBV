# Generated by Django 4.1.1 on 2022-09-10 14:45

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_film_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='poster',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
