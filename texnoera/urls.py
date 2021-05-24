"""texnoera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from kurs.views import kurs

urlpatterns = [
    path('admintexno/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^kurs/$', kurs, name='kurs'),
    path(r'xeber/', include('post.urls')),
    url(r'^melumat_bloku/$', melumat_bloku, name='melumat-bloku'),
    url(r'^tehsil/universitetler/$', universitetler, name='universitetler'),
    url(r'^tehsil/universitetler/ixtisaslar$', uni_ixtisaslar, name='uni_ixtisaslar'),
    url(r'^tehsil/kollecler/$', kollecler, name='kollecler'),
    url(r'^tehsil/kollecler/ixtisaslar$', kollec_ixtisaslar, name='kollec_ixtisaslar'),
    url(r'^tehsil/teqaudprogramlari/$', tequdprogramlari, name='teqaudprogramlari'),
    url(r'^iselanlari/vakansiyalar/$', vakansiylar, name='vakansiylar'),
    url(r'^iselanlari/tecrubeprogramlari/$', tecrubeprogramlari, name='tecrubeprogramlari'),
    url(r'^tedbirler/$', tedbirler, name='tedbirler'),
    url(r'^telimler/$', telimler, name='telimler'),
    url(r'^onlinekitabxana/$', onlinekitabxana, name='onlinekitabxana'),
    url(r'^tehsil/xaricdetehsil/$', xaricdetehsil, name='xaricdetehsil'),
    url(r'^haqqimizda/$', about, name='about'),
    url(r'^yandex_0185069037fc52ec.html/$', yandex, name='yandex'),
    url(r'^niyebiz/$', why, name='why'),
    url(r'^front/$', front, name='front'),
    url(r'^back/$', back, name='back'),
    url(r'^fullstack/$', fullstack, name='fullstack'),
    url(r'^ios/$', ios, name='ios'),
    url(r'^android/$', android, name='android'),
    url(r'^cross/$', cross, name='cross'),
    
    url(r'^devops/$', devops, name='devops'),
    url(r'^dataanaliz/$', dataanaliz, name='dataanaliz'),
    url(r'^uxui/$', uxui, name='uxui'),
    url(r'^qrafikdizayn/$', qrafik, name='qrafik'),
    url(r'^suni-intellekt/$', suni, name='suni'),
    url(r'^temir/$', temir, name='temir'),
    url(r'^axtaris/$', axtar, name='axtar'),
    url(r'^sistem-administratoru/$', sistem, name='sistem'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
