from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import kategori, aplikasi_utama

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def visidanmisi(request):
    template = loader.get_template('visidanmisi.html')
    return HttpResponse(template.render())

def pimpinanprodi(request):
    template = loader.get_template('pimpinanprodi.html')
    return HttpResponse(template.render())

def kurikulum(request):
    template = loader.get_template('kurikulum.html')
    return HttpResponse(template.render())

def dosen(request):
    template = loader.get_template('dosen.html')
    return HttpResponse(template.render())

def sap(request):
    template = loader.get_template('sap.html')
    return HttpResponse(template.render())

def organisasi(request):
    template = loader.get_template('organisasi.html')
    return HttpResponse(template.render())

def berita(request):
    template = loader.get_template('berita.html')
    return HttpResponse(template.render())

def jadwaluas(request):
    template = loader.get_template('jadwaluas')
    return HttpResponse(template.render())

def pengumuman(request):
    template = loader.get_template('pengumuman.html')
    return HttpResponse(template.render())



#def about(request):
    #data = aplikasi_utama.objects.all()
    #template = loader.get_template('about.html')
    #context = {
        #'text' : 'ini contoh',
        #'aplikasi_utama' : data,
    #}
   # return HttpResponse(template.render(context, request))
