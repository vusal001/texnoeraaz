from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models import  F
from .form import *
from django.core.mail import send_mail
from texnoera import settings

    
    





def home(request):
    posts= Xeber.objects.all()

    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    slider = Slider.objects.all()


    mobslider = Mobslider.objects.all()

    axtaris_posts = Xeber.objects.all()
    
    
    

    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)

   
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


 


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    contex = {
        'form': form,
        'post': posts,
        'reklamli': vip,
        'slider': slider,
        'mobslider': mobslider,
        'melumat': melumat_bloku,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
    }
    return render(request, 'home.html', contex)

def melumat_bloku(request):
    posts = Xeber.objects.filter(kategoriya='Məlumat bloku')

    content = 'Məlumat bloku'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
            # subject = form.cleaned_data['ad', '']
            text = form.cleaned_data['text']

            send_mail(text, from_email, ['info@texnoera.az'])


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()
        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)


    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')
    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 

def post_detail(request, id):

    post = get_object_or_404(Xeber, id=id)
    vip = Xeber.objects.filter(reklamli=True)

    posts = Xeber.objects.all().order_by('?')[:5]
    views = Xeber.objects.filter(id=post.id).update(views=F('views') + 1)


    reklam = Reklamlar.objects.all()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()
    contex = {
        'post': post,
        'reklamli': vip,
        'reklam': reklam,
        'posts': posts,
        'melumat': melumat_bloku,
        'form': form,
        
    }

    return render(request, 'detail.html', contex)


def universitetler(request):
    posts = Xeber.objects.filter(kategoriya='Universitetlər')

    content = 'Universitetlər'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()


    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()
        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)


    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()
    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 


def uni_ixtisaslar(request):
    posts = Xeber.objects.filter(kategoriya='Universitet ixtisasları')

    content = 'Universitet ixtisasları'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()


    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()
        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)


    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 



def kollecler(request):
    posts = Xeber.objects.filter(kategoriya='Kolleclər')

    content = 'Kolleclər'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()
        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)


    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)



    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 


def kollec_ixtisaslar(request):
    posts = Xeber.objects.filter(kategoriya='Kollec ixtisasları')

    content = 'Kollec ixtisasları'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()


    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()
        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)


    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 

def xaricdetehsil(request):
    posts = Xeber.objects.filter(kategoriya='Xaricdə təhsil')

    content = 'Xaricdə təhsil'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()
        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)


    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 

def tequdprogramlari(request):
    posts = Xeber.objects.filter(kategoriya='Təqaüd programları')

    content = 'Təqaüd programları'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 


def vakansiylar(request):
    posts = Xeber.objects.filter(kategoriya='Vakansiyalar')

    content = 'Vakansiyalar'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 

def tecrubeprogramlari(request):
    posts = Xeber.objects.filter(kategoriya='Təcrübə programları')

    content = 'Təcrübə programları'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()
        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)


    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 


def tedbirler(request):
    posts = Xeber.objects.filter(kategoriya='Tədbirlər')

    content = 'Tədbirlər'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 



def telimler(request):
    posts = Xeber.objects.filter(kategoriya='Təlimlər')

    content = 'Təlimlər'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex) 


def onlinekitabxana(request):
    posts = Onlinekitabxana.objects.all()

    content = 'Online kitabxana'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'onlinekitab.html', contex) 


def about(request):

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    return render(request, 'about.html', {'form': form})

def why(request):
    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
            # subject = form.cleaned_data['ad', '']
            text = form.cleaned_data['text']

            send_mail(text, from_email, ['info@texnoera.az'])

    return render(request, 'whyarewe.html', {'form': form})


# Create your views here.


def yandex(request):
    return render(request, 'yandex_0185069037fc52ec.html')




def front(request):
    posts = Xeber.objects.filter(kategoriya='Front-end')

    content = 'Front-end'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)



def back(request):
    posts = Xeber.objects.filter(kategoriya='Back-end')

    content = 'Back-end'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)



def fullstack(request):
    posts = Xeber.objects.filter(kategoriya='Full-stack')

    content = 'Full-stack'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)


def ios(request):
    posts = Xeber.objects.filter(kategoriya='IOS')

    content = 'IOS'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)



def android(request):
    posts = Xeber.objects.filter(kategoriya='Android')

    content = 'Android'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)


def cross(request):
    posts = Xeber.objects.filter(kategoriya='Cross')

    content = 'Cross'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)


def devops(request):
    posts = Xeber.objects.filter(kategoriya='DevOps')

    content = 'DevOps'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)



def dataanaliz(request):
    posts = Xeber.objects.filter(kategoriya='Data analiz')

    content = 'Data analiz'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)



def uxui(request):
    posts = Xeber.objects.filter(kategoriya='UX/UI')

    content = 'UX/UI'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)


def qrafik(request):
    posts = Xeber.objects.filter(kategoriya='Qrafik dizayn')

    content = 'Qrafik dizayn'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)


def sistem(request):
    posts = Xeber.objects.filter(kategoriya='Sistem admistratoru')

    content = 'Sistem admistratoru'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)



def suni(request):
    posts = Xeber.objects.filter(kategoriya='Süni intellekt')

    content = 'Süni intellekt'
    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()

    axtaris_posts = Xeber.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)



    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()


    melumat_bloku = Xeber.objects.filter(kategoriya='Məlumat bloku')

    contex = {
        'post': posts,
        'content' : content,
        'reklamli': vip,
        'reklam': reklam,
        'axtaris_posts': axtaris_posts,
        'form': form,
        'melumat': melumat_bloku,
    }

    return render(request, 'index.html', contex)



def temir(request):

    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    return render(request, 'temir.html', {'form': form})




def axtar(request):
    axtaris_posts = Xeber.objects.all()

    vip = Xeber.objects.filter(reklamli=True)

    reklam = Reklamlar.objects.all()


    post_query = request.GET.get('axtaris')


    if post_query:
        axtaris_posts = axtaris_posts.filter(
            Q(kategoriya__icontains=post_query) |
            Q(basliq__icontains=post_query) |
            Q(metin__icontains=post_query)
        ).distinct()

        page = request.GET.get('page', 1)
        paginator = Paginator(axtaris_posts, 10)
        try:
            axtaris_posts = paginator.page(page)
        except PageNotAnInteger:
            axtaris_posts = paginator.page(1)
        except EmptyPage:
            axtaris_posts = paginator.page(paginator.num_pages)


    if request.method == 'GET':
        form = Mail()
    
    else:
        form = Mail(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['mail']
                
            text = form.cleaned_data['text']
            subject = form.cleaned_data['ad']
            to = 'info@texnoera.az'
            send_mail(subject, text, from_email, [to])
            form = Mail()

    contex ={
        'axtaris_posts': axtaris_posts,
        'reklamli': vip,
        'reklam': reklam,
        'form': form,
    }

    return render(request, 'axtaris_netice.html', contex)







