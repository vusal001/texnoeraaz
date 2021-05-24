# Generated by Django 3.1.7 on 2021-04-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_slider_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='reklamlar',
            name='ustreklamlinkmon1',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Üst Mobil reklam linki 1'),
        ),
        migrations.AddField(
            model_name='reklamlar',
            name='ustreklamlinkmon2',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Üst Mobil reklam linki 2'),
        ),
        migrations.AddField(
            model_name='reklamlar',
            name='ustreklamlinkmon3',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Üst Mobil reklam linki 3'),
        ),
        migrations.AddField(
            model_name='reklamlar',
            name='ustreklammob1',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Üst Mobil reklam 1'),
        ),
        migrations.AddField(
            model_name='reklamlar',
            name='ustreklammob2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Üst Mobil reklam 2'),
        ),
        migrations.AddField(
            model_name='reklamlar',
            name='ustreklammob3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Üst Mobil reklam 3'),
        ),
        migrations.AlterField(
            model_name='xeber',
            name='kategoriya',
            field=models.CharField(choices=[('Xəbər', 'Xəbər'), ('İş elanları', (('Vakansiyalar', 'Vakansiyalar'), ('Təcrübə programları', 'Təcrübə programları'))), ('Təhsil', (('Universitetlər', 'Universitetlər'), ('Universitet ixtisasları', 'Universitet ixtisasları'), ('Kolleclər', 'Kolleclər'), ('Kollec ixtisasları', 'Kollec ixtisasları'), ('Xaricdə təhsil', 'Xaricdə təhsil'), ('Təqaüd programları', 'Təqaüd programları'))), ('Tədbirlər', (('Tədbirlər', 'Tədbirlər'), ('Təlimlər', 'Təlimlər'))), ('Məlumat bloku', (('Front-end', 'Front-end'), ('Back-end', 'Back-end'), ('Full-stack', 'Full-stack'), ('IOS', 'IOS'), ('Android', 'Android'), ('Cross', 'Cross'), ('DevOps', 'DevOps'), ('Data analiz', 'Data analiz'), ('UX/UI', 'UX/UI'), ('Qrafik dizayn', 'Qrafik dizayn'), ('süni intellekt', 'süni intellekt')))], max_length=25, verbose_name='Kategoriya'),
        ),
    ]