from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Charts
from api.serializers import ChartsSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs["content_type"] = "application/json"
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def chartList(request):
    if request.method == "GET":
        charts = Charts.objects.all()
        serialzer = ChartsSerializer(charts, many=True)
        return JSONResponse(serialzer.data)

    elif request.method == "POST":
        print(request.body)
        stream = BytesIO(request.body)
        print("Stream:", stream)
        data = JSONParser().parse(stream)
        print("data:", data)
        serializer = ChartsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

# Create your views here.
def index(request):
    jsonData = json.dumps({
        'text': 'this is supposed to be some text',
        'data': [
                {
                    'text': 'this is'
                },
                {
                    'text': 'is an '
                },
                {
                    'text': 'array of objects'
                }
            ],
        'number': 521,
        'bool': True
    })

    # return HttpResponse('Sup dude')
    return HttpResponse(jsonData, content_type='application/json' )
