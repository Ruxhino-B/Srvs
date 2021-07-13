from rest_framework import serializers
from .models import Lloj_Makine, Variant_Makine, Makina

class Lloj_makineSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','emer')
        model = Lloj_Makine

class Variant_MakineSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id','emer', 'lloi_makines')
        model = Variant_Makine

class MakinaSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('shasia', 'targa', 'lloji', 'varianti', 'tipi', 'viti_prodhimi', 'nr_sediljesh', 'nr_dyersh', 'kilometra', 'karburanti', 'kapaciteti', 'transmisioni', 'ngjyra', 'kualidimi', 'siguracioni', 'date_regjistrimi')
        model = Makina