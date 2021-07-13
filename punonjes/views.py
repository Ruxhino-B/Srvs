from rest_framework import generics
from .serializers import PunonjesSerializers
from .models import Punonjes
class PunonjesListVeiew(generics.ListAPIView):
    queryset = Punonjes.objects.all()
    serializer_class = PunonjesSerializers