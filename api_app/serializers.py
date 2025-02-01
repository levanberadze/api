from django.core.serializers import serialize
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


    def validate_engine_size(self, value):
        if value < 0: raise serializers.ValidationError('negative values are not allowed')
        return value