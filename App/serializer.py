from rest_framework import serializers
from .models import CalenderModel

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalenderModel
        fields = "__all__"