from rest_framework import serializers
from .models import Klient

class KlientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = '__all__'