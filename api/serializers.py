from rest_framework import serializers
from api.models import Charts
import json


class WritableJSONField(serializers.Field):
    """
    A custom field which subclasses `serializers.Field` class to easily
    serialize JSONField objects.
    """
    def to_internal_value(self, obj):
        return obj

    def to_representation(self, obj):
        return obj

# What we are doing here is to create a Serializer class for our Chart objects.
# To do this we use rest_framework's Django forms like sematics. The thing to note
# here is that the json data which contains the actual data for the charts should
# store a dict object directly as it handles the encoding and decoding on insert
# and query which is passed directly to the serializer by using our own custom
# field `WritableJSONField` which simply just passes the object without making
# any modifications to it. Whatever validation that we do want to perform we
# need to do it in our views where we have the logic to insert the data

class ChartsSerializer(serializers.Serializer):
    id =            serializers.IntegerField()
    chartName =     serializers.CharField(allow_blank=True, max_length=200)
    description =   serializers.CharField(allow_blank=True, max_length=800)
    isPrivate =     serializers.BooleanField(default=False)
    jsonData =      WritableJSONField()

    def create(self, validatedData):
        """
        Create and return a new `Charts` instance when given validated data
        """
        return Charts.objects.create(**validatedData)

    def update(self, instance, validatedData):
        """
        Update and return an existing `Charts` instance when given validated
        data
        """

        instance.chartName =    validatedData.get('ChartName')
        instance.description =  validatedData.get('description')
        instance.isPrivate =    validatedData.get('isPrivate')
        instance.jsonData =     validatedData.get('jsonData')
        instance.save()

        return instance

    class Meta:
        model = Charts
        fields = ('id', 'chartName', 'description', 'isPrivate', 'jsonData')
