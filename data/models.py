from django.db import models
from ckeditor.fields import RichTextField
from django.forms.widgets import NumberInput 
from django.contrib.auth.models import User

# Create your models here.

class Adminbem(models.Model):
    CATEGORY=( ('BEM-UNUJA', 'BEM-UNUJA'), ('BEMF-teknik' , 'BEMF-teknik'), ('BEMF-FAI' , 'BEMF-FAI'), ('BEMF-KES' , 'BEMF-KES'), ('BEMF-Soshum' , 'BEMF-Soshum'),)
    id_Adminbem = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    jenis_bem = models.CharField(max_length=200, blank=True, null=True)
    no_rekening = models.IntegerField(blank=True, null=True)
    telp_anggota =  models.IntegerField(blank=True, default='628')
    Email =  models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.jenis_bem)
    class Meta:
        verbose_name_plural ="Adminbem"


class tabelproposal(models.Model):
    CATEGORY=( ('diterima', 'diterima'), ('ditolak' , 'ditolak'), ('diperiksa' , 'diperiksa'), )
    CATEGORY1=( ('BEM-UNUJA', 'BEM-UNUJA'), ('BEMF-teknik' , 'BEMF-teknik'), ('BEMF-FAI' , 'BEMF-FAI'), ('BEMF-KES' , 'BEMF-KES'), ('BEMF-Soshum' , 'BEMF-Soshum'),)
    id_Adminbem = models.ForeignKey(Adminbem, blank=True, null= True, on_delete=models.SET_NULL)
    relasiproker = models.ForeignKey('proker', null=True, on_delete=models.SET_NULL)
    file = models.FileField(blank=True, null=True)
    acara = models.IntegerField(blank=True, null=True)
    konsumsi = models.IntegerField(blank=True, null=True)
    perlengkapan = models.IntegerField(blank=True, null=True)
    notifikasi = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    catatan = models.CharField(max_length=200, blank=True, null=True)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
        
class tabellaporan(models.Model):
    CATEGORY=( ('masih diperika' , 'masih diperika'),('AJUKAN ULANG', 'AJUKAN ULANG'), ('DITOLAK' , 'DITOLAK'), ('DITERIMA', 'DITERIMA'), )
    id_Adminbem = models.ForeignKey(Adminbem, blank=True, null= True, on_delete=models.SET_NULL)
    id_proker = models.ForeignKey('proker', null=True, on_delete=models.SET_NULL)
    id_berita = models.ForeignKey('berita', null=True, on_delete=models.SET_NULL)
    file = models.FileField(blank=True, default='erorfile.jpg')
    anggaran_dana = models.IntegerField(blank=True, null=True)
    waktu_pengumpulan = models.DateField(blank=True, null=True)
    tanggapan_laporan = models.CharField(max_length=200, blank=True, default='belum diperiksa', choices=CATEGORY)
    catatan = models.CharField(max_length=200, blank=True, default='tidak ada catatan')

class berita(models.Model):
    id_Adminbem = models.ForeignKey(Adminbem, blank=True, null= True, on_delete=models.SET_NULL)
    judul = models.CharField(max_length=200, blank=True, null=True)
    deskripsi = models.CharField(max_length=132, blank=True, null=True)
    isi = RichTextField(blank=True, null=True)
    gambar = models.ImageField(default='erorgambar.jpg', blank=True)
    date_created= models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.id_Adminbem, self.judul)
    class Meta:
        verbose_name_plural ="berita"

class coba(models.Model):
    id_Adminbem = models.ForeignKey(Adminbem, blank=True, null= True, on_delete=models.SET_NULL)
    img = models.ImageField(default='erorfile.jpg', blank=True)

class proker(models.Model):
    CATEGORY=( ('mingguan', 'mingguan'), ('bulanan' , 'bulanan'), ('tahunan' , 'tahunan'))
    CATEGORY1=( ('masih diperika' , 'masih diperika'),('DITERIMA', 'DITERIMA'), ('DITOLAK' , 'DITOLAK'), )
    CATEGORY2=( ('Dana BELUM CAIR' , 'Dana BELUM CAIR'),('Dana SUDAH CAIR', 'Dana SUDAH CAIR'),)
    id_Adminbem = models.ForeignKey(Adminbem, blank=True, null= True, on_delete=models.SET_NULL)
    relasi_proker = models.CharField(max_length=200, blank=True, null=True)
    devisi = models.CharField(max_length=200, blank=True, null=True)
    nama_kegiatan = models.CharField(max_length=200, blank=True, null=True)
    tujuan_kegiatan = models.CharField(max_length=200, blank=True, null=True)
    target_kegiatan = models.CharField(max_length=200, blank=True, null=True)
    waktu_kegiatan = models.DateField(blank=True, null=True)
    sifat_kegiatan = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    struktur_kepanitiaan = models.FileField(blank=True, default='erorfile.jpg')
    proposal_kegiatan = models.FileField(blank=True, default='erorfile.jpg')
    ringkasan_anggaran = models.IntegerField(blank=True, null=True)
    tanggapan_proker = models.CharField(max_length=200, blank=True, default='belum diperiksa', choices=CATEGORY1)
    catatan = models.CharField(max_length=200, blank=True, default='tidak ada catatan')
    terbitan_sk = models.FileField(blank=True, default='erorfile.jpg')
    pencairan_proker = models.CharField(max_length=200, blank=True, default='belum diputuskan', choices=CATEGORY2)

    def __str__(self):
        return '%s - %s' % (self.id_Adminbem, self.nama_kegiatan)
    class Meta:
        verbose_name_plural ="proker"

    
class sk(models.Model):
    CATEGORY=( ('masih diperika' , 'masih diperika'),('DITERIMA', 'DITERIMA'), ('DITOLAK' , 'DITOLAK'), )
    id_Adminbem = models.ForeignKey(Adminbem, blank=True, null= True, on_delete=models.SET_NULL)
    surat_permohonansk = models.FileField(blank=True, default='erorfile.jpg')
    struktur_anggota = models.FileField(blank=True, default='erorfile.jpg')
    periode = models.CharField(max_length=9, blank=True, default='2020-2021')
    visi_misi = RichTextField(blank=True, null=True)
    program_kerja = models.FileField(blank=True, default='erorfile.jpg')
    rab = models.FileField(blank=True, default='erorfile.jpg')
    total_rab = models.IntegerField(blank=True, null=True)
    tanggapan_sk = models.CharField(max_length=200, blank=True, default='belum diperiksa', choices=CATEGORY)
    catatan = models.CharField(max_length=200, blank=True, default='tidak ada catatan')
    terbitan_sk = models.FileField(blank=True, default='erorfile.jpg')

    def __str__(self):
        return '%s' % (self.id_Adminbem)
    class Meta:
        verbose_name_plural ="sk"

class aspirasi(models.Model):
    identitas = models.CharField(max_length=15, blank=True, default='Identitas-mu')
    komentar = models.CharField(max_length=100, blank=True, default='Isi disini')

    def __str__(self):
        return '%s' % (self.identitas)
    class Meta:
        verbose_name_plural ="aspirasi"

class download(models.Model):
    identitas = models.CharField(max_length=15, blank=True, default='Identitas-mu')
    komentar = models.CharField(max_length=100, blank=True, default='Isi disini')

    def __str__(self):
        return '%s' % (self.identitas)
    class Meta:
        verbose_name_plural ="aspirasi"

