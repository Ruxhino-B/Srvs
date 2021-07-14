from django.shortcuts import render
from rest_framework import generics
from .serializers import KategoriSherbimiSerializations, SherbimiSerializations, ShtoSherbimSerializations
from .models import Kategori_Sherbimi, Sherbimi, Shto_Sherbim

# Create your views here.

#Kategori Sherbimi
class KategoriListView(generics.ListAPIView):
    queryset = Kategori_Sherbimi.objects.all()
    serializer_class = KategoriSherbimiSerializations
class KategoriCreate(generics.CreateAPIView):
    serializer_class = KategoriSherbimiSerializations
class KategoriRetrive(generics.RetrieveAPIView):
    queryset = Kategori_Sherbimi.objects.all()
    serializer_class = KategoriSherbimiSerializations
class KategoriDestroye(generics.DestroyAPIView):
    serializer_class = KategoriSherbimiSerializations
class KategoriUpdate(generics.UpdateAPIView):
    serializer_class = KategoriSherbimiSerializations


#Sherbimi
class SherbimiListView(generics.ListAPIView):
    queryset = Sherbimi.objects.all()
    serializer_class = SherbimiSerializations
class SherbimCreate(generics.CreateAPIView):
    serializer_class = SherbimiSerializations
class SherbimRetrive(generics.RetrieveAPIView):
    queryset = Sherbimi.objects.all()
    serializer_class = SherbimiSerializations
class SherbimUpdate(generics.UpdateAPIView):
    serializer_class = SherbimiSerializations
class SherbimDestroye(generics.DestroyAPIView):
    serializer_class = SherbimiSerializations

#Shto Sherbim
class ShtimSherbimiListView(generics.ListAPIView):
    queryset = Shto_Sherbim.objects.all()
    serializer_class = ShtoSherbimSerializations
class ShtimSherbimiCreate(generics.CreateAPIView):
    serializer_class = ShtoSherbimSerializations
class ShtimSherbimiRetrive(generics.RetrieveAPIView):
    queryset = Shto_Sherbim.objects.all()
    serializer_class = ShtoSherbimSerializations
class ShtimSherbimiUpdate(generics.UpdateAPIView):
    serializer_class = ShtoSherbimSerializations
class ShtimSherbimiDestroye(generics.DestroyAPIView):
    serializer_class = ShtoSherbimSerializations