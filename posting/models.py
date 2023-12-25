from django.db import models


class kategori(models.Model):
    apple = models.CharField(max_length=100)
    lenovo = models.CharField(max_length=100)
    asus = models.CharField(max_length=100)


    def _str_(self):
        return f"{self.apple}"


class aplikasi_utama(models.Model):
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    toko = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.toko}"