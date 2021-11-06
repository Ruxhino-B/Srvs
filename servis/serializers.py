from rest_framework import serializers
from .models import Rezervim
from collections import OrderedDict

class RezervimSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super(RezervimSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
    class Meta:
        model = Rezervim
        fields = ('__all__')
