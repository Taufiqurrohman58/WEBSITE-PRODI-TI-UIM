
from django.contrib import admin
from.models import aplikasi_utama, kategori
from .models import Jadwal


class aplikasi_utamaAdmin(admin.ModelAdmin):
    list_display = ('toko',)


admin.site.register(aplikasi_utama, aplikasi_utamaAdmin)
admin.site.register(kategori)


class JadwalAdmin(admin.ModelAdmin):
    list_display="matkul1","matkul2","tanggal"

admin.site.register(Jadwal,JadwalAdmin)