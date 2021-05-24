# Generated by Django 3.1.7 on 2021-03-21 18:22

import ckeditor.fields
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=40, verbose_name='Ad soyad')),
                ('haqqinda', ckeditor.fields.RichTextField(verbose_name='Haqqında')),
                ('sekil', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=80, size=[1280, 720], upload_to='images/')),
                ('posting_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Mentor',
                'verbose_name_plural': 'Mentorlar',
            },
        ),
        migrations.CreateModel(
            name='mezunlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=40, verbose_name='Ad soyad')),
                ('haqqinda', ckeditor.fields.RichTextField(verbose_name='Haqqında')),
                ('sekil', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=80, size=[1280, 720], upload_to='images/')),
                ('posting_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Məzun',
                'verbose_name_plural': 'Məzunlar',
            },
        ),
        migrations.CreateModel(
            name='programlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basliq', models.CharField(max_length=40, verbose_name='Başlıq')),
                ('sekil', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=80, size=[1280, 720], upload_to='images/')),
                ('metin', ckeditor.fields.RichTextField(verbose_name='Mətin')),
                ('posting_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programlar',
            },
        ),
    ]