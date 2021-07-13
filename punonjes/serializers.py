from rest_framework import serializers
from .models import Punonjes

class PunonjesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Punonjes
