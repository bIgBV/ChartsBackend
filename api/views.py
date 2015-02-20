from django.http import HttpResponse
from django.utils.six import BytesIO
from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import Charts
from api.serializers import ChartsSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)

class ChartsList(APIView):
    def get(self, request, format=None):
        charts = Charts.objects.all()
        serialzer = ChartsSerializer(charts, many=True)
        return Response(serialzer.data)

    def post(self, request, format=None):
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        serializer = ChartsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EachChart(APIView):
    def getChart(self, chartId):
        """
        Retun an individual Chart object
        """
        try :
            return Charts.objects.get(id=chartId)
        except Charts.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        chart = self.getChart(id)
        serializer = ChartsSerializer(chart)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)
        chart = self.getChart(id)
        serializer = ChartsSerializer(chart, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        chart = self.getChart(id)
        chart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

