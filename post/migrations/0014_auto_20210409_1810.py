# Generated by Django 3.1.7 on 2021-04-09 14:10

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20210409_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xeber',
            name='sekil',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, size=[1920, 1080], upload_to='images/'),
        ),
    ]