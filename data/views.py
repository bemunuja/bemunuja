from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
# from reportlab.lib import pagesizes
from .filters import beritaFilter, berkasFilter, laporanFilter, prokerFilter, skFilter
from django.core.paginator import Paginator
# Create your views here.
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from .decorators import tolakhalaman_ini
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
from django.contrib.auth.models import Group
import csv


# coba admin BEM.....................................................................................
def formadminbem(request):
    data = Adminbem.objects.order_by('-id_Adminbem')
    context ={
        "menu" : 'Form Admn BEM',
        "page" : 'Form Admn BEM',
        'bem' : data
    }
    return render(request, 'data/adminbem/Formadminbem.html', context)

def inputadminbem(request):
    form = AdminbemForm()
    formadminbem = AdminbemForm(request.POST, request.FILES)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(username = username).first():
            messages.success(request, 'Username sudah ada.')
            return redirect('inputadminbem')

        if password1 != password2:
            messages.success(request, 'Password Tidak sama')
            return redirect('inputadminbem')
        # user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()
        # user
        # Group
        akses_bem = Group.objects.get(name='BEM')
        user.groups.add(akses_bem)
        # Group
        # Karyawan
        formsimpanadminbem = formadminbem.save()
        formsimpanadminbem.user = user
        formsimpanadminbem.save()
        # Karyawan
        return redirect('formadminbem')
    context ={
        "menu" : 'Input Form BEM',
        "page" : 'Input BEM',
        "form" : form   
    }
    return render(request, 'data/adminbem/inputadminbem.html', context)

# tampilan sistem informasi...........................................................................
def home(request):
    list_pusatberita = berita.objects.all
    p = Paginator(berita.objects.all(), 6)
    page = request.GET.get('page')
    venues = p.get_page(page)

    form = aspirasiForm()
    if request.method == 'POST':
        form = aspirasiForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('http://localhost:8000/')
    context = {
        'judul': 'BEM Universitas Nurul jadid | kabinet peradaban 2020-2021',
        'berita': list_pusatberita,
        'venues': venues,
        'pr': form,
        }
    return render(request, 'data/umum/dashboard.html', context)

def bemft(request):
    list_pusatberita = berita.objects.all
    p = Paginator(berita.objects.all(), 6)
    page = request.GET.get('page')
    venues = p.get_page(page)
    context = {
        'judul': 'BEM | Fakultas teknik Universitas Nurul jadid',
        'berita': list_pusatberita,
        'venues': venues
        }
    return render(request, 'data/umum/bemft.html', context)

def bemfai(request):
    list_pusatberita = berita.objects.all
    p = Paginator(berita.objects.all(), 6)
    page = request.GET.get('page')
    venues = p.get_page(page)
    context = {
        'judul': 'BEM | Fakultas agama islam Universitas Nurul jadid',
        'berita': list_pusatberita,
        'venues': venues
        }
    return render(request, 'data/umum/bemfai.html', context)

def bemfkes(request):
    list_pusatberita = berita.objects.all
    p = Paginator(berita.objects.all(), 6)
    page = request.GET.get('page')
    venues = p.get_page(page)
    context = {
        'judul': 'BEM | Fakultas kesehatan Universitas Nurul jadid',
        'berita': list_pusatberita,
        'venues': venues
        }
    return render(request, 'data/umum/bemfkes.html', context)

def bemfsoshum(request):
    list_pusatberita = berita.objects.all
    p = Paginator(berita.objects.all(), 6)
    page = request.GET.get('page')
    venues = p.get_page(page)
    context = {
        'judul': 'BEM | Fakultas Sosial Humaniora Universitas Nurul jadid',
        'berita': list_pusatberita,
        'venues': venues
        }
    return render(request, 'data/umum/bemfsoshum.html', context)

def aboutme(request):
    context = {
        'judul': 'Halaman tentang aplikasi',
        }
    return render(request, 'data/umum/aboutme.html', context)

def kontak(request):
    data = Adminbem.objects.all
    context = {
        'judul': 'Halaman kontak',
        'kontak': data,
        }
    return render(request, 'data/umum/kontak.html', context)

def profilsejarah(request):
    context = {
        'judul': 'Halaman profil sejarah',
        }
    return render(request, 'data/umum/profil_sejarah.html', context)

def profilstrukturbemu(request):
    data = sk.objects.all
    context = {
        'judul': 'Halaman profil struktural amggoota BEM-U',
        'struktur':data,
        }
    return render(request, 'data/umum/profil_strukturanggotabemu.html', context)

def galeri(request):
    list_galeri = coba.objects.all()
    p = Paginator(coba.objects.all(), 6)
    page = request.GET.get('page')
    venues = p.get_page(page)
    context = {
        'judul': 'Halaman galeri',
        'berita': list_galeri,
        'venues': venues
        }
    return render(request, 'data/umum/galeri.html', context)

def pusatberita(request):
    # list_pusatberita = berita.objects.order_by('-id')
    list_pusatberita = berita.objects.all()
    p = Paginator(berita.objects.all(), 6)
    page = request.GET.get('page')
    venues = p.get_page(page)
    context = {
        'judul': 'pusat berita',
        'berita': list_pusatberita,
        'venues': venues
        }
    return render(request, 'data/umum/pusatberita.html', context)

def berita1(request, pk):
    form = berita.objects.get(id=pk)
    context = {
        'judul': 'Form berita',
        'pr': form
    }
    return render(request, 'data/umum/berita1.html', context)

# tampilan form super admin.............................................................................
@login_required(login_url='login')
@pilihan_login
def tadmin(request):
    list_proposal = tabelproposal.objects.all()
    list_laporan = tabellaporan.objects.all()
    list_user = User.objects.all()
    list_proker = proker.objects.all()
    list_berita = berita.objects.all()
    total_proposal = list_proposal.count()
    total_laporan = list_laporan.count()
    total_user = list_user.count()
    total_proker = list_proker.count()
    total_berita = list_berita.count()
    data = {
        'judul': 'Halaman Suoer Admin',
        'data_total_proposal': total_proposal,
        'data_total_laporan': total_laporan,
        'data_total_user': total_user,
        'data_total_proker': total_proker,
        'data_total_berita': total_berita,
    }
    return render(request, 'data/admin/beranda.html', data)

def base(request):
    context = {
        'judul': 'Halaman admin',
        }
    return render(request, 'data/admin/base.html', context)

# ----------------------laporan------------------
def laporan(request):
    list_laporan = tabellaporan.objects.order_by('-id')
    filterlaporan = laporanFilter(request.GET, queryset=list_laporan)
    list_laporan = filterlaporan.qs
    context = {
        'judul': 'unggah lapporan',
        'laporan': list_laporan,
        'filter_laporan' : filterlaporan
        }
    return render(request, 'data/admin/laporan.html', context)

def tambahlaporan(request):
    form = formlaporan()
    if request.method == 'POST':
        form = formlaporan(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('laporan')
    context = {
        'judul': 'Form laporan',
        'pr':form,
    }
    return render(request, 'data/admin/tambah_laporan.html', context)

def updatelaporan(request, pk):
    order = tabellaporan.objects.get(id=pk) 
    form = formlaporan(instance=order)
    if request.method == 'POST': 
        formedit = formlaporan(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('laporan')
    context = {
        'judul': 'Edit laporan',
        'pr': form
        }
    return render(request, 'data/admin/tambah_laporan.html', context)

def deletelaporan(request, pk):
    laporanhapus = tabellaporan.objects.get(id=pk)
    if request.method == 'POST': 
        laporanhapus.delete() 
        return redirect('laporan')
    context = {
        'judul': 'hapus laporan',
        'datalaporandelete': laporanhapus,
        }
    return render(request, 'data/admin/delete_laporan.html', context)

# ----------------------proposal------------------
def proposal(request):
    list_berkas = tabelproposal.objects.order_by('-id')
    filterberkas = berkasFilter(request.GET, queryset=list_berkas)
    list_berkas = filterberkas.qs
    context = {
        'judul': 'unggah proposal',
        'berkas': list_berkas,
        'filter_berkas' : filterberkas,
        }
    return render(request, 'data/admin/proposal.html', context)

def tambahProposal(request):
    form = formproposal()
    if request.method == 'POST':
        form = formproposal(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('proposal')
    context = {
        'judul': 'Form proposal',
        'pr':form,
    }
    return render(request, 'data/admin/tambah_proposal.html', context)

def updateproposal(request, pk):
    order = tabelproposal.objects.get(id=pk) 
    form = formproposal(instance=order)
    if request.method == 'POST': 
        formedit = formproposal(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('proposal')
    context = {
        'judul': 'Edit proposal',
        'pr': form
        }
    return render(request, 'data/admin/tambah_proposal.html', context)

def deleteproposal(request, pk):
    proposalhapus = tabelproposal.objects.get(id=pk)
    if request.method == 'POST': 
        proposalhapus.delete() 
        return redirect('proposal')
    context = {
        'judul': 'hapus proposal',
        'dataproposaldelete': proposalhapus,
        }
    return render(request, 'data/admin/delete_proposal.html', context)

# ----------------------berita------------------
def tambahberita(request):
    form = formberita()
    if request.method == 'POST':
        form = formberita(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('adminberita')
    context = {
        'judul': 'Form berita',
        'pr':form,
    }
    return render(request, 'data/admin/tambah_berita.html', context)

def deleteberita(request, pk):
    beritahapus = berita.objects.get(id=pk)
    if request.method == 'POST': 
        beritahapus.delete() 
        return redirect('adminberita')
    context = {
        'judul': 'hapus berita',
        'databeritadelete': beritahapus,
        }
    return render(request, 'data/admin/delete_berita.html', context)

def adminberita(request):
    list_berita = berita.objects.order_by('-id')
    filterberita = beritaFilter(request.GET, queryset=list_berita)
    list_berita = filterberita.qs
    context = {
        'judul': 'Halaman Berita',
        'berita':list_berita,
        'filter_berita' : filterberita,
        }
    return render(request, 'data/admin/halaman_berita.html', context)

def updateberita(request, pk):
    order = berita.objects.get(id=pk) 
    form = formberita(instance=order)
    if request.method == 'POST': 
        formedit = formberita(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('adminberita')
    context = {
        'judul': 'Edit berita',
        'pr': form
        }
    return render(request, 'data/admin/coba_tambah.html', context)

# ----------------------proker------------------
@login_required(login_url='login')
def prokeradmin(request):
    list_proker = proker.objects.order_by('-id')
    context = {
        'judul': 'program kerja',
        'proker': list_proker,
        }
    return render(request, 'data/admin/proker.html', context)

@login_required(login_url='login')
def tambahprokeradmin(request):
    form = formproker()
    if request.method == 'POST':
        form = formproker(request.POST)
        if form.is_valid:
            form.save()
            return redirect('proker_admin')
    context = {
        'judul': 'Form proker',
        'pr':form,
    }
    return render(request, 'data/admin/tambah_proker.html', context)

@login_required(login_url='login')
def updateprokeradmin(request, pk):
    order = proker.objects.get(id=pk) 
    form = formproker(instance=order)
    if request.method == 'POST': 
        formedit = formproker(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('proker_admin')
    context = {
        'judul': 'Edit proker',
        'tampil': order,
        'pr': form
        }
    return render(request, 'data/admin/tambah_proker.html', context)

@login_required(login_url='login')
def deleteprokeradmin(request, pk):
    prokerhapus = proker.objects.get(id=pk)
    if request.method == 'POST': 
        prokerhapus.delete() 
        return redirect('proker_admin')
    context = {
        'judul': 'hapus proker',
        'dataprokerdelete': prokerhapus,
        }
    return render(request, 'data/admin/delete_proker.html', context)

# ----------------------User------------------
@login_required(login_url='login')
def tambahuser (request): 
    formregister = RegisterForm()
    if request.method == 'POST': 
        formregister = RegisterForm(request.POST) 
        if formregister.is_valid(): 
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername}')
            group_custumer = formregister.save()
            grup = Group.objects.get(name='BEM')
            group_custumer.groups.add(grup)
            return redirect('user')
    context = { 
        'judul': 'Halaman Register', 
        'menu': 'register', 
        'tampilregister' : formregister
    } 
    return render(request, 'data/admin/tambah_user.html', context)

@login_required(login_url='login')
def tambahuserbauk (request): 
    formregister = RegisterForm()
    if request.method == 'POST': 
        formregister = RegisterForm(request.POST) 
        if formregister.is_valid(): 
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername}')
            group_custumer = formregister.save()
            grup = Group.objects.get(name='BAUK')
            group_custumer.groups.add(grup)
            return redirect('user')
    context = { 
        'judul': 'Halaman Register', 
        'menu': 'register', 
        'tampilregister' : formregister
    } 
    return render(request, 'data/admin/tambah_user.html', context)

@login_required(login_url='login')
def user(request):
    list_userbem = User.objects.order_by('-id')
    context = {
        'judul': 'User',
        'userbem': list_userbem,
        }
    return render(request, 'data/admin/user.html', context)

@login_required(login_url='login')
def deleteuser(request, pk):
    userhapus = User.objects.get(id=pk)
    if request.method == 'POST': 
        userhapus.delete() 
        return redirect('user')
    context = {
        'judul': 'hapus user',
        'datauserdelete': userhapus,
        }
    return render(request, 'data/admin/delete_user.html', context)

# tampilan form Login & logout.............................................................................
def loginpage(request):
    formlogin = AuthenticationForm
    if request.method == 'POST': 
        username = request.POST.get('username') 
        password = request.POST.get('password')

        cocokan = authenticate(request, username=username, password=password )
        if cocokan is not None: 
            login(request, cocokan) 
            return redirect('tadmin')
    context = {
        'judul': 'Halaman Coba Admin',
        'tampillogin' : formlogin
    }
    return render(request, 'data/admin/halaman_login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('data')



# tampilan form user BEM.............................................................................
@login_required(login_url='login')
def bemPage(request):
    list_sk = sk.objects.all()
    list_laporan = tabellaporan.objects.all()
    list_user = User.objects.all()
    list_proker = proker.objects.all()
    list_berita = berita.objects.all()
    total_sk = list_sk.count()
    total_laporan = list_laporan.count()
    total_user = list_user.count()
    total_proker = list_proker.count()
    total_berita = list_berita.count()
    context = {
        'judul': 'bempage',
        'data_total_sk': total_sk,
        'data_total_laporan': total_laporan,
        'data_total_user': total_user,
        'data_total_proker': total_proker,
        'data_total_berita': total_berita,
    }
    return render(request, 'data/BEM/user.html', context)

def pusatprokerBEM(request):
    list_proker = proker.objects.order_by('-id')
    filterproker = prokerFilter(request.GET, queryset=list_proker)
    list_proker = filterproker.qs
    context = {
        'judul': 'program kerja',
        'proker': list_proker,
        'filter_proker' : filterproker,
        }
    return render(request, 'data/BEM/prokerBEM.html', context)

@login_required(login_url='login')
def tambahProker(request):
    form = formproker()
    if request.method == 'POST':
        form = formproker(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('proker_BEM')
    context = {
        'judul': 'Form proposal',
        'pr':form,
    }
    return render(request, 'data/BAUK/tambahprokerBEM_BAUK.html', context)

def statusproker(request, pk):
    order = proker.objects.get(id=pk)
    context = {
        'judul': 'Edit proker',
        'tampil': order,
        }
    return render(request, 'data/BEM/statusproker_BEM.html', context)

def statuslaporanbem(request, pk):
    form = tabellaporan.objects.get(id=pk)
    context = {
        'judul': 'status laporan',
        'tampil': form
        }
    return render(request, 'data/BEM/status_laporanBEM.html', context)

def laporanbem(request):
    list_laporan = tabellaporan.objects.order_by('-id')
    filterlaporan = berkasFilter(request.GET, queryset=list_laporan)
    list_laporan = filterlaporan.qs
    context = {
        'judul': 'laporan BEM',
        'laporan': list_laporan,
        'filter_laporan' : filterlaporan,
        }
    return render(request, 'data/BEM/laporanBEM.html', context)

def tambahlaporanbem(request):
    form = formlaporan()
    if request.method == 'POST':
        form = formlaporan(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('laporanBEMBEM')
    context = {
        'judul': 'Form laporan',
        'pr':form,
    }
    return render(request, 'data/BEM/tambah_laporanBEM.html', context)









def proposalbem(request):
    list_berkas = tabelproposal.objects.order_by('-id')
    filterberkas = berkasFilter(request.GET, queryset=list_berkas)
    list_berkas = filterberkas.qs
    context = {
        'judul': 'proposal BEM',
        'berkas': list_berkas,
        'filter_berkas' : filterberkas,
        }
    return render(request, 'data/BEM/proposalBEM.html', context)

def statusproposalbem(request, pk):
    form = tabelproposal.objects.get(id=pk)
    context = {
        'judul': 'status proposal',
        'pr': form
        }
    return render(request, 'data/BEM/status_proposalBEM.html', context)

def tambahProposalbem(request):
    form = formproposalbem()
    if request.method == 'POST':
        form = formproposalbem(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('proposalBEMBEM')
    context = {
        'judul': 'Form proposal',
        'pr':form,
    }
    return render(request, 'data/BEM/tambah_proposalBEM.html', context)

# tampilan form BAUK.............................................................................
@login_required(login_url='login')
def baukPage(request):
    list_sk = sk.objects.all()
    list_laporan = tabellaporan.objects.all()
    list_user = User.objects.all()
    list_proker = proker.objects.all()
    list_berita = berita.objects.all()
    total_sk = list_sk.count()
    total_laporan = list_laporan.count()
    total_user = list_user.count()
    total_proker = list_proker.count()
    total_berita = list_berita.count()
    context = {
        'judul': 'baukPage',
        'data_total_sk': total_sk,
        'data_total_laporan': total_laporan,
        'data_total_user': total_user,
        'data_total_proker': total_proker,
        'data_total_berita': total_berita,
    }
    return render(request, 'data/BAUK/beranda_BAUK.html', context)

def pusatsk(request):
    list_sk = sk.objects.order_by('-id')
    filtersk = skFilter(request.GET, queryset=list_sk)
    list_sk = filtersk.qs
    context = {
        'judul': 'pengajuan sk',
        'sk': list_sk,
        'filter_sk' : filtersk,
        }
    return render(request, 'data/BAUK/sk.html', context)

def pusatsk_bem(request):
    list_sk = sk.objects.order_by('-id')
    filtersk = skFilter(request.GET, queryset=list_sk)
    list_sk = filtersk.qs
    context = {
        'judul': 'pengajuan sk',
        'sk': list_sk,
        'filter_sk' : filtersk,
        }
    return render(request, 'data/BEM/sk_bem.html', context)

def tambahsk(request):
    form = formsk()
    if request.method == 'POST':
        form = formsk(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('skBEM_BEM')
    context = {
        'judul': 'ajukan sk',
        'pr':form,
    }
    return render(request, 'data/BEM/tambahsk_bem.html', context)

def tanggapansk(request, pk):
    order = sk.objects.get(id=pk) 
    form = formtanggapansk(instance=order)
    if request.method == 'POST': 
        formedit = formtanggapansk(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('skBEM_BAUK')
    context = {
        'judul': 'tanggapan sk',
        'tampil': order,
        'pr': form
        }
    return render(request, 'data/BAUK/tanggapan_sk.html', context)

def detailsk(request, pk):
    order = sk.objects.get(id=pk) 
    form = formtanggapansk(instance=order)
    if request.method == 'POST': 
        formedit = formtanggapansk(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('skBEM_BAUK')
    context = {
        'judul': 'detail proker',
        'tampil': order,
        'pr': form
        }
    return render(request, 'data/BAUK/detail_sk.html', context)

def statussk(request, pk):
    order = sk.objects.get(id=pk)
    context = {
        'judul': 'detail proker',
        'tampil': order,
        }
    return render(request, 'data/BEM/statussk.html', context)

def deletesk(request, pk):
    skhapus = sk.objects.get(id=pk)
    if request.method == 'POST': 
        skhapus.delete() 
        return redirect('skBEM_BAUK')
    context = {
        'judul': 'hapus sk',
        'dataskdelete': skhapus,
        }
    return render(request, 'data/BAUK/hapus_sk.html', context)

@login_required(login_url='login')
def pusatproker(request):
    list_proker = proker.objects.order_by('-id')
    filterproker = prokerFilter(request.GET, queryset=list_proker)
    list_proker = filterproker.qs
    context = {
        'judul': 'program kerja',
        'proker': list_proker,
        'filter_proker' : filterproker,
        }
    return render(request, 'data/BAUK/prokerBEM_BAUK.html', context)

def proposalbem(request):
    list_berkas = tabelproposal.objects.order_by('-id')
    filterberkas = berkasFilter(request.GET, queryset=list_berkas)
    list_berkas = filterberkas.qs
    context = {
        'judul': 'proposal BEM',
        'berkas': list_berkas,
        'filter_berkas' : filterberkas,
        }
    return render(request, 'data/BEM/proposalBEM.html', context)

@login_required(login_url='login')
def updateproker(request, pk):
    order = proker.objects.get(id=pk) 
    form = formproker(instance=order)
    if request.method == 'POST': 
        formedit = formproker(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('prokerBEM_BAUK')
    context = {
        'judul': 'Edit proker',
        'pr': form
        }
    return render(request, 'data/BAUK/tambahprokerBEM_BAUK.html', context)

def detailproker(request, pk):
    order = proker.objects.get(id=pk) 
    form = formtanggapanproker(instance=order)
    if request.method == 'POST': 
        formedit = formtanggapanproker(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('prokerBEM_BAUK')
    context = {
        'judul': 'Edit proker',
        'tampil': order,
        'pr': form
        }
    return render(request, 'data/BAUK/detailproker_BAUK.html', context)

def tanggapanproker(request, pk):
    order = proker.objects.get(id=pk) 
    form = formtanggapanproker(instance=order)
    if request.method == 'POST': 
        formedit = formtanggapanproker(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('prokerBEM_BAUK')
    context = {
        'judul': 'Edit proker',
        'tampil': order,
        'pr': form
        }
    return render(request, 'data/BAUK/tanggapanproker.html', context)

@login_required(login_url='login')
def deleteproker(request, pk):
    prokerhapus = proker.objects.get(id=pk)
    if request.method == 'POST': 
        prokerhapus.delete() 
        return redirect('prokerBEM_BAUK')
    context = {
        'judul': 'hapus proker',
        'dataprokerdelete': prokerhapus,
        }
    return render(request, 'data/BAUK/hapusprokerBEM_BAUK.html', context)

@login_required(login_url='login')
def registerPage (request): 
    formregister = RegisterForm()
    if request.method == 'POST': 
        formregister = RegisterForm(request.POST) 
        if formregister.is_valid(): 
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername}')
            group_custumer = formregister.save()
            grup = Group.objects.get(name='BEM')
            group_custumer.groups.add(grup)
            return redirect('userbem')
    context = { 
        'judul': 'Halaman Register', 
        'menu': 'register', 
        'tampilregister' : formregister
    } 
    return render(request, 'data/admin/halaman_register.html', context)

@login_required(login_url='login')
def userBem(request):
    list_userbem = User.objects.order_by('-id')
    context = {
        'judul': 'program kerja',
        'userbem': list_userbem,
        }
    return render(request, 'data/BAUK/userBEM_BAUK.html', context)

@login_required(login_url='login')
def deleteuserbauk(request, pk):
    userhapus = User.objects.get(id=pk)
    if request.method == 'POST': 
        userhapus.delete() 
        return redirect('userbem')
    context = {
        'judul': 'hapus user',
        'datauserdelete': userhapus,
        }
    return render(request, 'data/BAUK/hapususerBEM_BAUK.html', context)

@login_required(login_url='login')
def proposalbauk(request):
    list_berkas = tabelproposal.objects.order_by('-id')
    filterberkas = berkasFilter(request.GET, queryset=list_berkas)
    list_berkas = filterberkas.qs
    context = {
        'judul': 'proposal BAUK',
        'berkas': list_berkas,
        'filter_berkas' : filterberkas,
        }
    return render(request, 'data/BAUK/proposalBEM_BAUK.html', context)

@login_required(login_url='login')
def tanggapanproposalbauk(request, pk):
    order = tabelproposal.objects.get(id=pk) 
    form = formnotifproposal(instance=order)
    if request.method == 'POST': 
        formedit = formnotifproposal(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('proposal_bauk')
    context = {
        'judul': 'Edit proposal',
        'pr': form
        }
    return render(request, 'data/BAUK/tanggapanproposal_BAUK.html', context)

@login_required(login_url='login')
def hapusproposalbauk(request, pk):
    proposalhapus = tabelproposal.objects.get(id=pk)
    if request.method == 'POST': 
        proposalhapus.delete() 
        return redirect('proposal_bauk')
    context = {
        'judul': 'hapus proposal',
        'dataproposaldelete': proposalhapus,
        }
    return render(request, 'data/BAUK/hapusproposal_BAUK.html', context)

@login_required(login_url='login')
def laporanbauk(request):
    list_laporan = tabellaporan.objects.order_by('-id')
    filterlaporan = laporanFilter(request.GET, queryset=list_laporan)
    list_laporan = filterlaporan.qs
    context = {
        'judul': 'proposal BAUK',
        'laporan': list_laporan,
        'filter_laporan' : filterlaporan,
        }
    return render(request, 'data/BAUK/laporanBEM_BAUK.html', context)

@login_required(login_url='login')
def detailaporanbauk(request, pk):
    order = tabellaporan.objects.get(id=pk) 
    form = formnotiflaporan(instance=order)
    if request.method == 'POST': 
        formedit = formnotiflaporan(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('laporan_bauk')
    context = {
        'judul': 'Edit laporan',
        'tampil': order,
        'pr': form
        }
    return render(request, 'data/BAUK/detaillaporan.html', context)

def tanggapanaporanbauk(request, pk):
    order = tabellaporan.objects.get(id=pk) 
    form = formtanggapanlaporan(instance=order)
    if request.method == 'POST': 
        formedit = formtanggapanlaporan(request.POST, request.FILES, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('laporan_bauk')
    context = {
        'judul': 'Edit laporan',
        'tampil': order,
        'pr': form
        }
    return render(request, 'data/BAUK/tanggapanlaporanBEM_BAUK.html', context)

@login_required(login_url='login')
def hapuslaporanbauk(request, pk):
    laporanhapus = tabellaporan.objects.get(id=pk)
    if request.method == 'POST': 
        laporanhapus.delete() 
        return redirect('laporan_bauk')
    context = {
        'judul': 'hapus laporan',
        'datalaporandelete': laporanhapus,
        }
    return render(request, 'data/BAUK/hapuslaporan_BAUK.html', context)

# cetak exel.............................................................................
def cetakproposal(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data proposal.csv'
    writer = csv.writer(response)
    b = tabelproposal.objects.all()
    writer.writerow(['pengunggah', 'bem', 'relasiproker', 'file', 'acara', 'konsumsi', 'perlengkapan', 'notifikasi', 'catatan'])
    for data in b:
        writer.writerow([data.pengunggah, data.bem, data.relasiproker, data.file, data.acara, data.konsumsi, data.perlengkapan, data.notifikasi, data.catatan, ])
    return response

def cetaklaporan(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data laporan.csv'
    writer = csv.writer(response)
    b = tabellaporan.objects.all()
    writer.writerow(['id_Adminbem', 'id_proker', 'id_berita', 'anggaran_dana', 'waktu_pengumpulan'])
    for data in b:
        writer.writerow([data.id_Adminbem, data.id_proker, data.id_berita, data.anggaran_dana, data.waktu_pengumpulan ])
    return response

def cetakproker(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=data kegiatan.csv'
    writer = csv.writer(response)
    b = proker.objects.order_by('-id')
    writer.writerow([
        'BEM', 
        'devisi', 
        'nama anggota', 
        'Email', 
        'No telepon', 
        'No rekening', 
        'nama kegiatan', 
        'tujuan kegiatan',
        'target kegiatan',
        'waktu kegiatan',
        'sifat kegiatan',
        'proposal kegiatan',
        ])
    for data in b:
        writer.writerow([
            data.id_Adminbem, 
            data.devisi,
            data.id_Adminbem.Email, 
            data.id_Adminbem.telp_anggota, 
            data.id_Adminbem.no_rekening, 
            data.nama_kegiatan, 
            data.tujuan_kegiatan, 
            data.target_kegiatan, 
            data.waktu_kegiatan, 
            data.sifat_kegiatan,
            data.proposal_kegiatan, 
            ])
    return response

def viewcoba(request):
    c = coba.objects.order_by('-id')
    context = {
        'judul': 'image',
        'image': c,
        }
    return render(request, 'data/admin/coba.html', context)

def tambahcoba(request):
    form = formberita()
    if request.method == 'POST':
        form = formberita(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('adminberita')
    context = {
        'judul': 'Form coba',
        'pr':form,
    }
    return render(request, 'data/admin/coba_tambah.html', context)

def tambahgaleri(request):
    form = formcoba()
    if request.method == 'POST':
        form = formcoba(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('coba')
    context = {
        'judul': 'Form coba',
        'pr':form,
    }
    return render(request, 'data/admin/coba_tambah.html', context)
    
def deletegaleri(request, pk):
    galerihapus = coba.objects.get(id=pk)
    if request.method == 'POST': 
        galerihapus.delete() 
        return redirect('form_coba')
    context = {
        'judul': 'hapus berita',
        'datagaleridelete': galerihapus,
        }
    return render(request, 'data/BEM/hapus_galeriBEM.html', context)