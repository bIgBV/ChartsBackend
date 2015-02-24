from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Charts

class ChartsSerializer(serializers.ModelSerializer):
    jsonData = serializers.ListField(child=serializers.DictField())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Charts
        fields = ('id', 'chartName', 'description', 'isPrivate', 'jsonData', 'owner')

class UserSerializer(serializers.ModelSerializer):
    charts = serializers.PrimaryKeyRelatedField(many=True, queryset=Charts.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'charts')
