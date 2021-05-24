# Generated by Django 3.1.7 on 2021-04-09 13:00

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20210408_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobslider',
            name='sekil',
            field=models.FileField(upload_to='images/', verbose_name='Şəkil'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='sekil',
            field=models.FileField(upload_to='images/', verbose_name='Şəkil'),
        ),
        migrations.AlterField(
            model_name='xeber',
            name='sekil',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=80, size=[1920, 1080], upload_to='images/'),
        ),
    ]
