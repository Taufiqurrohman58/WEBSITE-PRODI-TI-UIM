from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import kategori, aplikasi_utama
from .models import Jadwal

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

def berita1(request):
    template = loader.get_template('berita1.html')
    return HttpResponse(template.render())

def berita2(request):
    template = loader.get_template('berita2.html')
    return HttpResponse(template.render())

def berita3(request):
    template = loader.get_template('berita3.html')
    return HttpResponse(template.render())

def berita4(request):
    template = loader.get_template('berita4.html')
    return HttpResponse(template.render())

def berita5(request):
    template = loader.get_template('berita5.html')
    return HttpResponse(template.render())

def berita6(request):
    template = loader.get_template('berita6.html')
    return HttpResponse(template.render())

def berita7(request):
    template = loader.get_template('berita7.html')
    return HttpResponse(template.render())

def berita8(request):
    template = loader.get_template('berita8.html')
    return HttpResponse(template.render())

def berita9(request):
    template = loader.get_template('berita9.html')
    return HttpResponse(template.render())

def berita10(request):
    template = loader.get_template('berita10.html')
    return HttpResponse(template.render())

def berita2(request):
    template = loader.get_template('berita2.html')
    return HttpResponse(template.render())

def berita3(request):
    template = loader.get_template('berita3.html')
    return HttpResponse(template.render())

def berita4(request):
    template = loader.get_template('berita4.html')
    return HttpResponse(template.render())

def berita5(request):
    template = loader.get_template('berita5.html')
    return HttpResponse(template.render())

def berita6(request):
    template = loader.get_template('berita6.html')
    return HttpResponse(template.render())

def berita7(request):
    template = loader.get_template('berita7.html')
    return HttpResponse(template.render())

def berita8(request):
    template = loader.get_template('berita8.html')
    return HttpResponse(template.render())

def berita9(request):
    template = loader.get_template('berita9.html')
    return HttpResponse(template.render())

def berita10(request):
    template = loader.get_template('berita10.html')
    return HttpResponse(template.render())

def beritapage2(request):
    template = loader.get_template('berita-page2.html')
    return HttpResponse(template.render())

def beritapage3(request):
    template = loader.get_template('berita-page3.html')
    return HttpResponse(template.render())

def jadwaluas(request):
    mem=Jadwal.objects.all()
    return render(request,'jadwaluas.html',{'mem':mem})

def add(request):
    return render (request,'add.html')

def addrec(request):
    x=request.POST['matkul1']
    y=request.POST['matkul2']
    z=request.POST['tanggal']
    mem=Jadwal(matkul1=x,matkul2=y,tanggal=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Jadwal.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Jadwal.objects.get(id=id)
    return render(request, 'update.html', {'mem': mem})


def uprec(request,id):
    x=request.POST['matkul1']
    y=request.POST['matkul2']
    z=request.POST['tanggal']
    mem=Jadwal.objects.get(id=id)
    mem.matkul1=x
    mem.matkul2=y
    mem.tanggal=z
    mem.save()
    return redirect("/")

def pengumuman(request):
    template = loader.get_template('pengumuman.html')
    return HttpResponse(template.render())

def programpembelajaran(request):
    template = loader.get_template('programbljr.html')
    return HttpResponse(template.render())



#def about(request):
    #data = aplikasi_utama.objects.all()
    #template = loader.get_template('about.html')
    #context = {
        #'text' : 'ini contoh',
        #'aplikasi_utama' : data,
    #}
   # return HttpResponse(template.render(context, request))
