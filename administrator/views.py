from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from servis.models import Shto_Sherbim
from servis.serializers import RezervimSerializer
from sherbim.serializers import ShtoSherbimSerializations


# Sherbim i pa aprovuar
class ShtimSherbimiPaAprovuarListView(generics.ListCreateAPIView):
    queryset = Shto_Sherbim.sherbimPaAprovuar.all()
    serializer_class = ShtoSherbimSerializations


class ShtimSherbimiPaPaguarListView(generics.ListCreateAPIView):
    queryset = Shto_Sherbim.sherbimPaPaguar.all()
    serializer_class = ShtoSherbimSerializations
