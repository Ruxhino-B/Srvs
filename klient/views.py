from rest_framework import generics
from django.shortcuts import render
from .models import Klient
# Create your views here.
from .serializers import KlientSerializers

class KlientListView(generics.ListAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializers

class KlientListCreateApiView(generics.CreateAPIView):
    serializer_class = KlientSerializers

class KlientListDelete(generics.DestroyAPIView):
    serializer_class = KlientSerializers

class KlientRetrive(generics.RetrieveAPIView):
    serializer_class = KlientSerializers
    queryset = Klient.objects.all()
class KlientUpdate(generics.UpdateAPIView):
    serializer_class = KlientSerializers

