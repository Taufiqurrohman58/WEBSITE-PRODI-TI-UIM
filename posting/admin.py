
from django.contrib import admin
from.models import aplikasi_utama, kategori


class aplikasi_utamaAdmin(admin.ModelAdmin):
    list_display = ('toko',)


admin.site.register(aplikasi_utama, aplikasi_utamaAdmin)
admin.site.register(kategori)