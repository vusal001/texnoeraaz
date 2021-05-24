from django.shortcuts import render
from .models import *

def kurs(request):

    program = programlar.objects.all()

    mentorlar = mentor.objects.all()

    telebeler =  mezunlar.objects.all()

    contex ={
        'programlar': program,
        'mentorlar': mentorlar,
        'telebeler': telebeler,
    }

    return render(request, 'kurs.html', contex)







# Create your views here.
