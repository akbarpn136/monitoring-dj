from django.db import models
from django.core.validators import URLValidator


# Create your models here.
class DaerahObjek(models.Model):
    nama_objek = models.CharField(verbose_name='Nama Observasi Objek', max_length=200)
    nama_daerah = models.CharField(verbose_name='Daerah', max_length=100)

    def __str__(self):
        return self.nama_objek


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
    daerah = models.ForeignKey(DaerahObjek, verbose_name='Daerah', null=True, blank=True, on_delete=models.SET_NULL,
                               default=1)

    class Meta:
        ordering = ('tanggal',)

    def __str__(self):
        return 'Grup kecepatan: ' + str(self.grup_kecepatan)


class PilihanVisualisasi(models.Model):
    nama = models.CharField(verbose_name='Nama Grafik', max_length=180)
    info = models.CharField(verbose_name='Info Singkat', max_length=200)
    deskripsi = models.TextField(verbose_name='Deskripsi Grafik')
    thumb = models.TextField(verbose_name='Link Thumbnail', validators=[URLValidator()])
    daerah = models.ForeignKey(DaerahObjek, verbose_name='Daerah', null=True, blank=True, on_delete=models.SET_NULL,
                               default=1)

    KOSONG = ''
    ATRIBUT_ANGIN = 'ATR'
    PDF_ANGIN = 'PDF'
    WINDROSE = 'WRS'
    WATERFALL = 'WTR'
    RMS = 'RMS'
    PILIHAN_JENIS = (
        (KOSONG, '-----'),
        (ATRIBUT_ANGIN, 'Atribut Angin'),
        (PDF_ANGIN, 'Grafik PDF'),
        (WINDROSE, 'Grafik Windrose'),
        (WATERFALL, 'Grafik Waterfall'),
        (RMS, 'Grafik RMS'),
    )

    jenis = models.CharField(verbose_name='Jenis Grafik', max_length=3, default=KOSONG, choices=PILIHAN_JENIS)

    def __str__(self):
        return self.nama
