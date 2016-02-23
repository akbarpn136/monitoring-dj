from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class DataAngin(models.Model):
    tanggal = models.DateField(verbose_name='Tanggal Pengukuran')
    waktu = models.TimeField(verbose_name='Waktu Pengukuran', max_length=100)
    arah = models.FloatField(verbose_name='Arah Angin (satuan sudut)')
    kompas = models.CharField(verbose_name='Simbol Arah (kompas)', max_length=3)
    kecepatan = models.FloatField(verbose_name='Kecepatan Angin (m/s)')
    grup_kecepatan = models.FloatField(verbose_name='Kelompok Kecepatan Angin (m/s)')
    akselerator1 = models.FloatField(verbose_name='Akselerator 1')
    akselerator2 = models.FloatField(verbose_name='Akselerator 2')
    akselerator3 = models.FloatField(verbose_name='Akselerator 3')
    akselerator4 = models.FloatField(verbose_name='Akselerator 4')
    akselerator5 = models.FloatField(verbose_name='Akselerator 5')

    def __str__(self):
        return 'Grup kecepatan: ' + str(self.grup_kecepatan)


class PilihanVisualisasi(models.Model):
    nama = models.CharField(verbose_name='Nama Grafik', max_length=180)
    info = models.CharField(verbose_name='Info Singkat', max_length=200)
    deskripsi = models.TextField(verbose_name='Deskripsi Grafik')
    thumb = models.TextField(verbose_name='Link Thumbnail', validators=[URLValidator()])

    def __str__(self):
        return self.nama
