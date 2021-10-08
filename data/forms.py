from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class FileInput(forms.FileInput):
    input_type = 'file'

class aspirasiForm(ModelForm):
    class Meta:
        model = aspirasi
        fields= ['identitas', 'komentar']

        widgets = {
            'identitas': forms.TextInput(attrs={'class': 'form-control'}),
            'komentar': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'identitas': 'a',
            'komentar': 'b',
        }

class AdminbemForm(ModelForm):
    class Meta:
        model = Adminbem
        fields= ['jenis_bem', 'Email','telp_anggota','no_rekening']

        widgets = {
            'jenis_bem': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'no_rekening': forms.TextInput(attrs={'class': 'form-control'}),
            'telp_anggota': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'jenis_bem': 'BEM',
            'Email': 'Email',
            'no_rekening': 'No Rekening',
            'nama_anggota': 'Nama Anggota ',
            'telp_anggota': 'Nomor telefon',
        }

class formproposal(ModelForm):
    class Meta:
        model = tabelproposal
        fields= ['id_Adminbem','relasiproker','file','acara','konsumsi','perlengkapan']
        widgets = { 
            'id_Adminbem': forms.Select(attrs={'class': 'form-control'}),
            'relasiproker': forms.Select(attrs={'class': 'form-control'}),
            'acara': forms.TextInput(attrs={'class': 'form-control'}),
            'konsumsi': forms.TextInput(attrs={'class': 'form-control'}),
            'perlengkapan': forms.TextInput(attrs={'class': 'form-control'})
        } 
        labels = { 
            'id_Adminbem': 'pengunggah',
            'relasiproker': 'program kerja',
            'waktu': 'waktu pelaksanaan',
            'file': 'Berkas Proposal',
            'acara': 'Devisi Acara',
            'konsumsi': 'Devisi konsimsi',
            'perlengkapan': 'Devisi perlengkapan',
        }

class formproposalbem(ModelForm):
    class Meta:
        model = tabelproposal
        fields= ['id_Adminbem','relasiproker','file','acara','konsumsi','perlengkapan']
        widgets = { 
            'id_Adminbem': forms.Select(attrs={'class': 'form-control'}),
            'relasiproker': forms.Select(attrs={'class': 'form-control'}),
            'acara': forms.TextInput(attrs={'class': 'form-control'}),
            'konsumsi': forms.TextInput(attrs={'class': 'form-control'}),
            'perlengkapan': forms.TextInput(attrs={'class': 'form-control'})
        } 
        labels = { 
            'id_Adminbem': 'pengunggah',
            'relasiproker': 'program kerja',
            'waktu': 'waktu pelaksanaan',
            'file': 'Berkas Proposal',
            'acara': 'Devisi Acara',
            'konsumsi': 'Devisi konsimsi',
            'perlengkapan': 'Devisi perlengkapan',
        }

class formlaporanbem(ModelForm):
    class Meta:
        model = tabellaporan
        fields= '__all__'
        widgets = { 
        } 
        labels = { 
        }

class formnotifproposal(ModelForm):
    class Meta:
        model = tabelproposal
        fields= ['notifikasi','catatan']
        widgets = { 
            'notifikasi': forms.Select(attrs={'class': 'form-control'}),
            'catatan': forms.Textarea(attrs={'class': 'form-control'}),
        } 
        labels = { 
            'notifikasi': 'Notifikasi',
            'catatan': 'Catatan',
        }

class formnotiflaporan(ModelForm):
    class Meta:
        model = tabellaporan
        fields= '__all__'
        widgets = { 
        } 
        labels = { 
        }

class formlaporan(ModelForm):
    class Meta:
        model = tabellaporan
        fields= ['id_proker','id_berita','file', 'waktu_pengumpulan', 'anggaran_dana']
        widgets = { 
            'id_proker': forms.Select(attrs={'class': 'form-control'}),
            'id_berita': forms.Select(attrs={'class': 'form-control'}),
            'file': FileInput(attrs={'class': 'form-control'}),
            'waktu_pengumpulan': DateInput(attrs={'class': 'form-control'}),
            'anggaran_dana': forms.TextInput(attrs={'class': 'form-control'}),
        } 
        labels = { 
            'id_proker': 'Program kerja',
            'id_berita': 'Bukti publikasi kegiatan',
            'file': 'File LPJ     :',
            'waktu_pengumpulan': 'Waktu pengumpulan',
            'anggaran_dana': 'Rincian penggunaan dana',
        }

class formtanggapanlaporan(ModelForm):
    class Meta:
        model = tabellaporan
        fields= ['tanggapan_laporan','catatan']
        widgets = { 
            'tanggapan_laporan': forms.Select(attrs={'class': 'form-control'}),
            'catatan': forms.Textarea(attrs={'class': 'form-control'}),
        } 
        labels = { 
            'tanggapan_laporan': 'Status',
            'catatan': 'Catatan',
        }

class formproker(ModelForm):
    class Meta:
        model = proker
        fields= ['id_Adminbem','devisi','nama_kegiatan', 'tujuan_kegiatan', 'target_kegiatan', 'waktu_kegiatan', 'sifat_kegiatan', 'struktur_kepanitiaan', 'proposal_kegiatan','ringkasan_anggaran', ]
        widgets = { 
            'id_Adminbem': forms.Select(attrs={'class': 'form-control'}),
            'devisi': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_kegiatan': forms.TextInput(attrs={'class': 'form-control'}),
            'tujuan_kegiatan': forms.Textarea(attrs={'class': 'form-control'}),
            'target_kegiatan': forms.TextInput(attrs={'class': 'form-control'}),
            'waktu_kegiatan': DateInput(attrs={'class': 'form-control'}),
            'sifat_kegiatan': forms.Select(attrs={'class': 'form-control'}),
            'struktur_kepanitiaan': FileInput(attrs={'class': 'form-control'}),
            'proposal_kegiatan': FileInput(attrs={'class': 'form-control'}),
            'ringkasan_anggaran': forms.TextInput(attrs={'class': 'form-control'}),
            
        } 
        labels = {
            'id_Adminbem': 'Proker dari BEM',
            'devisi': 'Nama Menteri/devisi',
            'nama_kegiatan': 'Nama kegiatan',
            'tujuan_kegiatan': 'tujuan kegiatan',
            'target_kegiatan': 'target kegiatan',
            'waktu_kegiatan': 'wajtu kegiatan',
            'sifat_kegiatan': 'sifat kegiatan',
            'struktur_kepanitiaan': 'struktur kepanitiaan',
            'proposal_kegiatan': 'File proposal',
            'ringkasan_anggaran': 'Total tansaksi dana',
        }

class formtanggapanproker(ModelForm):
    class Meta:
        model = proker
        fields= ['tanggapan_proker','catatan','terbitan_sk', 'pencairan_proker']
        widgets = { 
            'tanggapan_proker': forms.Select(attrs={'class': 'form-control'}),
            'catatan': forms.Textarea(attrs={'class': 'form-control'}),
            'pencairan_proker': forms.Select(attrs={'class': 'form-control'}),
            
        } 
        labels = {
            'tanggapan_proker': 'Tanggapan',
            'catatan': 'catatan',
            'terbitan_sk': 'Terbitkan SK panitia',
            'pencairan_proker': 'Status Dana kegiatan',
        }

class formberita(ModelForm):
    class Meta:
        model = berita
        fields= ['id_Adminbem', 'judul', 'deskripsi', 'isi', 'gambar']
        widgets = { 
            'id_Adminbem': forms.Select(attrs={'class': 'form-control'}),
            'bem': forms.Select(attrs={'class': 'form-control'}),
            'id_Adminbem': forms.Select(attrs={'class': 'form-control'}),
            'judul': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'isi': forms.Textarea(attrs={'class': 'form-control'})
        } 
        labels = { 
            'id_Adminbem': 'Pengunggah',
            'bem': 'tag BEM',
            'id_Adminbem': 'tag BEM id',
            'judul': 'Judul berita',
            'deskripsi': 'Deskripsi singkat',
            'isi': 'isi berita',
            'gambar': 'gambar berita',
        }

class formcoba(ModelForm):
    class Meta:
        model = coba
        fields= '__all__'
        widgets = { 
        } 
        labels = { 
            'img': 'tambahkan gambar',
        }

class formuserbem(ModelForm):
    class Meta:
        model = User
        fields= '__all__'
        widgets = { 
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.Textarea(attrs={'class': 'form-control'}),
            'password1': forms.Textarea(attrs={'class': 'form-control'}),
            'password2': forms.Textarea(attrs={'class': 'form-control'}),
        } 
        labels = { 
            'username': 'username BEM',
            'email': 'email BEM',
            'password1': 'password',
            'password2': 'ulang password',
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields= ['username','email','password1','password2']

class formsk(ModelForm):
    class Meta:
        model = sk
        fields= ['id_Adminbem','surat_permohonansk','struktur_anggota', 'periode', 'visi_misi', 'program_kerja', 'rab', 'total_rab']
        widgets = { 
            'id_Adminbem': forms.Select(attrs={'class': 'form-control'}),
            'surat_permohonansk': FileInput(attrs={'class': 'form-control'}),
            'struktur_anggota': FileInput(attrs={'class': 'form-control'}),
            'periode': forms.TextInput(attrs={'class': 'form-control'}),
            'program_kerja': FileInput(attrs={'class': 'form-control'}),
            'rab': FileInput(attrs={'class': 'form-control'}),
            'total_rab': forms.TextInput(attrs={'class': 'form-control'}),
            'target_kegiatan': forms.TextInput(attrs={'class': 'form-control'})
            
        } 
        labels = {
            'id_Adminbem': 'BEM',
            'surat_permohonansk': 'surat permohonan SK',
            'struktur_anggota': 'Struktur keanggotaan',
            'periode': 'periode',
            'visi_misi': 'Visi dan Misi',
            'program_kerja': 'program kerja',
            'rab': 'Rencana anggran belanja',
            'total_rab': 'Total RAB'
        }

class formtanggapansk(ModelForm):
    class Meta:
        model = sk
        fields= ['tanggapan_sk','catatan','terbitan_sk']
        widgets = { 
            'tanggapan_sk': forms.Select(attrs={'class': 'form-control'}),
            'catatan': forms.Textarea(attrs={'class': 'form-control'}),
            'terbitan_sk': FileInput(attrs={'class': 'form-control'}),
            
        } 
        labels = {
            'tanggapan_sk': 'Tanggapan',
            'catatan': 'catatan',
            'terbitan_sk': 'terbitan_sk pengurusan BEM',
        }