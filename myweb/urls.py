from django.contrib import admin
from django.urls import path, include
from posting.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index' ),
    path('visidanmisi/', visidanmisi, name='visidanmisi' ),
    path('pimpinanprodi/', pimpinanprodi, name='pimpinanprodi' ),
    path('kurikulum/', kurikulum, name='kurikulum' ),
    path('dosen/', dosen, name='dosen' ),
    path('sap/', sap, name='sap' ),
    path('organisasi/', organisasi, name='organisasi' ),
    path('berita/', berita, name='berita' ),
    path('Program Kemitraan Masyarakat (PKM) UIM Gelar Workshop Digital Marketing, Copywriting, dan Digital Branding bagi Relawan Penjaga Pantai dan Laut di Madura/', berita1, name='berita1' ),
    path('HIMA Teknik Informatika Fakultas Teknik UIM Gelar Pelatihan Sekaligus Launching Website/', berita2, name='berita2' ),
    path('Evaluasi Kinerja Prodi TI dan SI Mendapatkan Apresiasi Unggul Oleh LPMI UIM./', berita3, name='berita3' ),
    path('Dosen Teknik Informatika dan Sistem Informasi Menghibahkan Buku Ajar ke Perpustakaan UIM Pamekasan./', berita4, name='berita4' ),
    path('Sources For Digital Marketing/', berita5, name='berita5' ),
    path('Stories About Digital Marketing/', berita6, name='berita6' ),
    path('The Big Thing in Digital Marketing/', berita7, name='berita7' ),
    path('Will Digital Marketing Ever Rule/', berita8, name='berita8' ),
    path('Digital Marketing: Expectations/', berita9, name='berita9' ),
    path('Digital Marketing Explained/', berita10, name='berita10' ),
    path('berita/page2/', beritapage2, name='beritapage2' ),
    path('berita/page3/', beritapage3, name='beritapage3' ),
    path('jadwaluas/', jadwaluas, name='jadwaluas' ),
    path('add/', add, name='add'),
    path('addrec/', addrec, name='addrec'),
    path('jadwaluas/delete/<int:id>/', delete, name='delete'), 
    path('jadwaluas/update/<int:id>/',update,name='update'),
    path('jadwaluas/update/uprec/<int:id>/',uprec,name='uprec'),
    path('pengumuman/', pengumuman, name='pengumuman' ),
    path('program pembelajaran/', programpembelajaran, name='program pembelajaran' ),

]
