from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from api.models import Charts
from api.serializers import ChartsSerializer
from api.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ChartsList(generics.ListCreateAPIView):
    queryset = Charts.objects.all()
    serializer_class = ChartsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class EachCharts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Charts.objects.all()
    serializer_class = ChartsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
