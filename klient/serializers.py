from rest_framework import serializers
from .models import Klient

class KlinetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'