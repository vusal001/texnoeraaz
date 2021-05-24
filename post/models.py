from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField
from django.urls import reverse
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Xeber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=1, null=True, related_name='posts', verbose_name='Istifadeci')

    KAT=(
        ('Xəbər', 'Xəbər'),
        ('İş elanları', (
            ('Vakansiyalar', 'Vakansiyalar'),
            ('Təcrübə programları', 'Təcrübə programları'),
        )),
        ('Təhsil', (
            ('Universitetlər', 'Universitetlər'),
            ('Universitet ixtisasları', 'Universitet ixtisasları'),
            ('Kolleclər', 'Kolleclər'),
            ('Kollec ixtisasları', 'Kollec ixtisasları'),
            ('Xaricdə təhsil', 'Xaricdə təhsil'),
            ('Təqaüd programları', 'Təqaüd programları'),
        )),
        ('Tədbirlər', (
            ('Tədbirlər', 'Tədbirlər'),
            ('Təlimlər', 'Təlimlər'),
        )),
        ('Məlumat bloku', (
            ('Front-end', 'Front-end'),
            ('Back-end', 'Back-end'),
            ('Full-stack', 'Full-stack'),
            ('IOS', 'IOS'),
            ('Android', 'Android'),
            ('Cross', 'Cross'),
            ('DevOps', 'DevOps'),
            ('Data analiz', 'Data analiz'),
            ('UX/UI', 'UX/UI'),
            ('Qrafik dizayn', 'Qrafik dizayn'),
            ('Sistem administratoru', 'Sistem administratoru'),
            ('Süni intellekt', 'Süni intellekt'),
        )),
    )

    kategoriya = models.CharField(max_length=25, choices=KAT, verbose_name="Kategoriya")

    sekil = ResizedImageField(size=[1920, 1080], quality=100, upload_to='images/')


    thumbnail = ImageSpecField(source='sekil', processors=[ResizeToFill(1280, 720)], format='JPEG', options={'quality': 90})

    basliq = models.CharField(max_length=100, verbose_name="Başlıq")

    
    metin = RichTextField(verbose_name='Mətin')

    xeber = models.BooleanField(default=True, verbose_name="Xəbərlər bölümünə düşsün")

    reklamli = models.BooleanField(default=False, verbose_name="Xüsusi elan")


    posting_date = models.DateTimeField(auto_now_add=True)


    views =  models.IntegerField(default=1 ,verbose_name='Baxış sayı', blank=True, null=True)

    def __str__(self):
        return self.basliq
    
    class Meta:
        ordering = ['-posting_date']
        verbose_name = 'Xəbər'
        verbose_name_plural = 'Xəbərlər'


    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})


class Onlinekitabxana(models.Model):
    basliq = models.CharField(verbose_name='Başlıq', max_length=100)

    sekil = ResizedImageField(size=[1280, 720], quality=80, upload_to='images/')

    pdf = models.FileField(verbose_name="Pdf faylı")

    metin = RichTextField(verbose_name='Açığlama', blank=True, null=True)

    posting_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.basliq

    class Meta:
        
        verbose_name = 'Kitab'
        verbose_name_plural = 'Onlayn kitabxana'


class Reklamlar(models.Model):
    ustreklam1 = models.FileField(verbose_name='Üst reklam 1', blank=True, null=True)
    ustreklamlink1 = models.CharField(verbose_name='Üst reklam linki 1', max_length=1000, blank=True, null=True) 
    


    ustreklam2 = models.FileField(verbose_name='Üst reklam 2', blank=True, null=True)
    ustreklamlink2 = models.CharField(verbose_name='Üst reklam linki 2', max_length=1000, blank=True, null=True) 
  
    ustreklam3 = models.FileField(verbose_name='Üst reklam 3', blank=True, null=True)
    ustreklamlink3 = models.CharField(verbose_name='Üst reklam linki 3', max_length=1000, blank=True, null=True) 

    ustreklammob1 = models.FileField(verbose_name='Üst Mobil reklam 1', blank=True, null=True)
    ustreklamlinkmon1 = models.CharField(verbose_name='Üst Mobil reklam linki 1', max_length=1000, blank=True, null=True) 
    ustreklamtxt1 = models.CharField(verbose_name='Üst Mobil reklam text 1', max_length=100, blank=True, null=True)

    ustreklammob2 = models.FileField(verbose_name='Üst Mobil reklam 2', blank=True, null=True)
    ustreklamlinkmon2 = models.CharField(verbose_name='Üst Mobil reklam linki 2', max_length=1000, blank=True, null=True) 
    ustreklamtxt2 = models.CharField(verbose_name='Üst Mobil reklam text 2', max_length=100, blank=True, null=True)


    ustreklammob3 = models.FileField(verbose_name='Üst Mobil reklam 3', blank=True, null=True)
    ustreklamlinkmon3 = models.CharField(verbose_name='Üst Mobil reklam linki 3', max_length=1000, blank=True, null=True) 
    ustreklamtxt3 = models.CharField(verbose_name='Üst Mobil reklam text 3', max_length=100, blank=True, null=True)




    ustyan = models.FileField(verbose_name='Üst yan', blank=True, null=True)
    ustyanlink = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Üst yan link')

    altyan = models.FileField(verbose_name='Alt yan', blank=True, null=True)
    altyanlink = models.CharField(max_length=1000, verbose_name='Alt yan link', blank=True, null=True)

    detailust = models.FileField(verbose_name='Xəbər üst', blank=True, null=True)
    detailustlink = models.CharField(max_length=1000,verbose_name='Xəbər üst link', blank=True, null=True)

    detailalt = models.FileField(verbose_name='Xəbər alt', blank=True, null=True)
    detailaltlink = models.CharField(max_length=1000, verbose_name='Xəbər alt link', blank=True, null=True)   

    def __str__(self):
        return "Reklam"
    

    class Meta:
        
        verbose_name = 'Reklam'
        verbose_name_plural = 'Reklam'
        

class Slider(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True, verbose_name='Başlıq')
    txt = models.CharField(max_length=200, blank=True, null=True, verbose_name='Metn')
    sekil = models.FileField(verbose_name='Şəkil', upload_to='images/')
    link = models.CharField(verbose_name='Link', max_length=1000, blank=True, null=True) 
    posting_date = models.DateTimeField(auto_now_add=True)
    
    


    class Meta:
        
        verbose_name = 'Slide'
        verbose_name_plural = 'Slider'


class Mobslider(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True, verbose_name='Başlıq')
    txt = models.CharField(max_length=200, blank=True, null=True, verbose_name='Metn')
    sekil = models.FileField(verbose_name='Şəkil', upload_to='images/')
    link = models.CharField(verbose_name='Link', max_length=1000, blank=True, null=True) 
    posting_date = models.DateTimeField(auto_now_add=True)
    
    


    class Meta:
        
        verbose_name = 'Mobil Slide'
        verbose_name_plural = 'Mobil Slider'

# Create your models here.
