from django.db import models


# Create your models here.
class DataAngin(models.Model):
    tanggal = models.CharField(verbose_name='Tanggal Pengukuran', max_length=100)
    waktu = models.CharField(verbose_name='Waktu Pengukuran', max_length=100)
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
        return self.tanggal + ' ' + str(self.grup_kecepatan)
