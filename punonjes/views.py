from rest_framework import generics
from .serializers import PunonjesSerializers
from .models import Punonjes

class PunonjesListVeiew(generics.ListAPIView):
    queryset = Punonjes.objects.all()
    serializer_class = PunonjesSerializers

class PunonjesCreate(generics.CreateAPIView):
    serializer_class = PunonjesSerializers

class PunonjesRetrive(generics.RetrieveAPIView):
    queryset = Punonjes.objects.all()
    serializer_class = PunonjesSerializers

class PunonjesDestroy(generics.DestroyAPIView):
    serializer_class = PunonjesSerializers

class PunonjesUpdate(generics.UpdateAPIView):
    serializer_class = PunonjesSerializers