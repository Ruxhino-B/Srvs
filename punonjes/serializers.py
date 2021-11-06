from rest_framework import serializers
from .models import Punonjes, Roli


class RoliSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Roli

class PunonjesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Punonjes

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['roli'] = RoliSerializers(instance.roli).data
        return rep
