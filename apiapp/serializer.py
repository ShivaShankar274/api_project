from apiapp.models import apimodel
from rest_framework import serializers

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = apimodel
        fields = '__all__'