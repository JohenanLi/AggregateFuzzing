from .models import usedSoft,codeResult
from rest_framework import serializers
class UsedSoftSer(serializers.ModelSerializer):
    class Meta:
        model = usedSoft
        fields = '__all__'

class ResultSer(serializers.ModelSerializer):
    class Meta:
        model = codeResult
        fields = '__all__'