from rest_framework import serializers

from .models import ASInfo

class ASInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ASInfo
        fields = ['range_start', 'range_end', 'as_number', 'country_code', 'as_description']