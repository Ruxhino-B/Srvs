from django.shortcuts import render
from rest_framework import generics
from .models import Lloj_Makine, Variant_Makine, Makina
from .serializers import Lloj_makineSerializers, Variant_MakineSerializers, MakinaSerializers
# Create your views here.

#Lloj_Makine
class Lloj_makineSerializersListView(generics.ListAPIView):
    queryset = Lloj_Makine.objects.all()
    serializer_class = Lloj_makineSerializers
class LlojMakineCreate(generics.CreateAPIView):
    serializer_class = Lloj_makineSerializers
class Lloj_makineRetrive(generics.RetrieveAPIView):
    serializer_class = Lloj_makineSerializers
class Lloj_makineUpdate(generics.UpdateAPIView):
    serializer_class = Lloj_makineSerializers
class Lloj_makineDestoy(generics.DestroyAPIView):
    serializer_class = Lloj_makineSerializers


#Variant Makine
class VariantMakineSerializersListView(generics.ListAPIView):
    queryset = Variant_Makine.objects.all()
    serializer_class = Variant_MakineSerializers
class VariantMakineCreate(generics.CreateAPIView):
    serializer_class = Variant_MakineSerializers
class VariantMakineRetrive(generics.RetrieveAPIView):
    queryset = Variant_Makine.objects.all()
    serializer_class = Variant_MakineSerializers
class VariantMakineUpdate(generics.UpdateAPIView):
    serializer_class = Variant_MakineSerializers
class VariantMakineDestroy(generics.DestroyAPIView):
    serializer_class = Variant_MakineSerializers

#Makine
class MakineSerializerListView(generics.ListAPIView):
    queryset = Makina.objects.all()
    serializer_class = MakinaSerializers
class MakineCreate(generics.CreateAPIView):
    serializer_class = MakinaSerializers
class MakineRetrive(generics.RetrieveAPIView):
    serializer_class = MakinaSerializers
    queryset = Makina.objects.all()
class MakineUpdate(generics.UpdateAPIView):
    serializer_class = MakinaSerializers
class MakineDestroy(generics.RetrieveAPIView):
    serializer_class = MakinaSerializers