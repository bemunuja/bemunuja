import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class berkasFilter(django_filters.FilterSet):
    pengunggah = CharFilter(field_name="id_Adminbem", lookup_expr='icontains')

    class Meta: 
        model = tabelproposal
        fields =['id_Adminbem']

class prokerFilter(django_filters.FilterSet):
    pengunggah = CharFilter(field_name="id_Adminbem", lookup_expr='icontains')

    class Meta: 
        model = proker
        fields =['id_Adminbem']

class laporanFilter(django_filters.FilterSet):
    pengunggah = CharFilter(field_name="id_proker", lookup_expr='icontains')

    class Meta: 
        model = tabellaporan
        fields =['id_proker']

class beritaFilter(django_filters.FilterSet):
    judul = CharFilter(field_name="judul", lookup_expr='icontains')

    class Meta: 
        model = berita
        fields =['judul']

class skFilter(django_filters.FilterSet):
    pengunggah = CharFilter(field_name="id_Adminbem", lookup_expr='icontains')

    class Meta: 
        model = berita
        fields =['id_Adminbem']