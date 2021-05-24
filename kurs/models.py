from django.db import models
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField



class programlar(models.Model):
    basliq = models.CharField(max_length=40, verbose_name="Başlıq")
    
    sekil = ResizedImageField(size=[1280, 720], quality=80, upload_to='images/')
    
    metin = RichTextField(verbose_name='Mətin')

    posting_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.basliq
    
    class Meta:
        verbose_name = 'Program'
        verbose_name_plural = 'Programlar'


class mentor(models.Model):
    adi =  models.CharField(max_length=40, verbose_name="Ad soyad")   

    haqqinda = RichTextField(verbose_name="Haqqında")

    sekil =  ResizedImageField(size=[1280, 720], quality=80, upload_to='images/')

    posting_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adi
    
    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentorlar'

        

class mezunlar(models.Model):
    adi =  models.CharField(max_length=40, verbose_name="Ad soyad")   

    haqqinda = RichTextField(verbose_name="Haqqında")

    sekil =  ResizedImageField(size=[1280, 720], quality=80, upload_to='images/')

    posting_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adi
    
    class Meta:
        verbose_name = 'Məzun'
        verbose_name_plural = 'Məzunlar'



# Create your models here.
