from rest_framework import generics
from django.shortcuts import render
from .models import Klient
# Create your views here.
from .serializers import KlinetSerializers

class KlientListView(generics.ListAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlinetSerializers
