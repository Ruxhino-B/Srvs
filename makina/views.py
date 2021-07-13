from django.shortcuts import render
from rest_framework import generics
from .models import Lloj_Makine, Variant_Makine, Makina
from .serializers import Lloj_makineSerializers, Variant_MakineSerializers, MakinaSerializers
# Create your views here.

class Lloj_makineSerializersListView(generics.ListAPIView):
    queryset = Lloj_Makine.objects.all()
    serializer_class = Lloj_makineSerializers

class VariantMakineSerializersListView(generics.ListAPIView):
    queryset = Variant_Makine.objects.all()
    serializer_class = Variant_Makine

class MakineSerializerListView(generics.ListAPIView):
    queryset = Makina.objects.all()
    serializer_class = MakinaSerializers