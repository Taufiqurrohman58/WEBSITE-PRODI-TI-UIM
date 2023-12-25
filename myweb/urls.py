from django.contrib import admin
from django.urls import path
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
    path('jadwaluas/', jadwaluas, name='jadwaluas' ),
    path('pengumuman/', pengumuman, name='pengumuman' ),
]
