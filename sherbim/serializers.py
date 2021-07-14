from rest_framework import serializers
from .models import Kategori_Sherbimi, Sherbimi, Shto_Sherbim

class KategoriSherbimiSerializations(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Kategori_Sherbimi

class SherbimiSerializations(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Sherbimi

class ShtoSherbimSerializations(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Shto_Sherbim