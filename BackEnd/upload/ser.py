from .models import usedSoft
from rest_framework import serializers
class UsedSoftSer(serializers.ModelSerializer):
    class Meta:
        model = usedSoft
        fields = '__all__'