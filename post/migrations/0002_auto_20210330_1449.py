# Generated by Django 3.1.7 on 2021-03-30 10:49

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onlinekitabxana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basliq', models.CharField(max_length=100, verbose_name='Başlıq')),
                ('pdf', models.FileField(upload_to='', verbose_name='Pdf faylı')),
                ('metin', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Açığlama')),
                ('posting_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Kitab',
                'verbose_name_plural': 'Onlayn kitabxana',
            },
        ),
        migrations.CreateModel(
            name='Reklamlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ustreklam1', models.FileField(blank=True, null=True, upload_to='', verbose_name='Üst reklam 1')),
                ('ustreklamlink1', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Üst reklam linki 1')),
                ('ustreklam2', models.FileField(blank=True, null=True, upload_to='', verbose_name='Üst reklam 2')),
                ('ustreklamlink2', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Üst reklam linki 2')),
                ('ustreklam3', models.FileField(blank=True, null=True, upload_to='', verbose_name='Üst reklam 3')),
                ('ustreklamlink3', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Üst reklam linki 3')),
                ('ustyan', models.FileField(blank=True, null=True, upload_to='', verbose_name='Üst yan')),
                ('ustyanlink', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Üst yan link')),
                ('altyan', models.FileField(blank=True, null=True, upload_to='', verbose_name='Alt yan')),
                ('altyanlink', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Alt yan link')),
                ('detailust', models.FileField(blank=True, null=True, upload_to='', verbose_name='Xəbər üst')),
                ('detailustlink', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Xəbər üst link')),
                ('detailalt', models.FileField(blank=True, null=True, upload_to='', verbose_name='Xəbər alt')),
                ('detailaltlink', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Xəbər alt link')),
            ],
            options={
                'verbose_name': 'Reklam',
                'verbose_name_plural': 'Reklam',
            },
        ),
        migrations.AlterModelOptions(
            name='xeber',
            options={'ordering': ['-posting_date'], 'verbose_name': 'Xəbər', 'verbose_name_plural': 'Xəbərlər'},
        ),
        migrations.AddField(
            model_name='xeber',
            name='metin',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now, verbose_name='Mətin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xeber',
            name='posting_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xeber',
            name='reklamli',
            field=models.BooleanField(default=False, verbose_name='Xüsusi elan'),
        ),
        migrations.AddField(
            model_name='xeber',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Istifadeci'),
        ),
        migrations.AddField(
            model_name='xeber',
            name='xeber',
            field=models.BooleanField(default=True, verbose_name='Xəbərlər bölümünə düşsün'),
        ),
        migrations.AlterField(
            model_name='xeber',
            name='basliq',
            field=models.CharField(max_length=100, verbose_name='Başlıq'),
        ),
    ]
