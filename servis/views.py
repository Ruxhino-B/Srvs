from django.shortcuts import render
from rest_framework import generics
from .models import Rezervim
from .serializers import RezervimSerializer
# Create your views here.


class RezervimListApi(generics.ListAPIView):
    serializer_class = RezervimSerializer
    queryset = Rezervim.objects.all()
class RezervimRetriveApi(generics.RetrieveAPIView):
    serializer_class = RezervimSerializer
    queryset = Rezervim.objects.all()
class RezervimCreateApi(generics.CreateAPIView):
    serializer_class = RezervimSerializer
    queryset = Rezervim.objects.all()
class RezervimUpdateApi(generics.UpdateAPIView):
    serializer_class = RezervimSerializer
    queryset = Rezervim.objects.all()
class RezervimDestroyApi(generics.DestroyAPIView):
    serializer_class = RezervimSerializer
    queryset = Rezervim.objects.all()
