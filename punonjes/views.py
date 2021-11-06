from rest_framework import generics
from .serializers import PunonjesSerializers, RoliSerializers
from .models import Punonjes, Roli

class PunonjesListVeiew(generics.ListAPIView):
    queryset = Punonjes.objects.all()
    serializer_class = PunonjesSerializers

class PunonjesCreate(generics.CreateAPIView):
    serializer_class = PunonjesSerializers
    queryset = Punonjes.objects.all()

class PunonjesRetrive(generics.RetrieveAPIView):
    queryset = Punonjes.objects.all()
    serializer_class = PunonjesSerializers

class PunonjesDestroy(generics.DestroyAPIView):
    serializer_class = PunonjesSerializers
    queryset = Punonjes.objects.all()

class PunonjesUpdate(generics.UpdateAPIView):
    serializer_class = PunonjesSerializers

class RoliListVeiw(generics.ListAPIView):
    queryset = Roli.objects.all()
    serializer_class = RoliSerializers

class RoliCreate(generics.CreateAPIView):
    serializer_class = RoliSerializers

class RoliUpdate(generics.UpdateAPIView):
    serializer_class = RoliSerializers
    queryset = Roli.objects.all()

class RoliDestroy(generics.DestroyAPIView):
    serializer_class = RoliSerializers
    queryset = Roli.objects.all()