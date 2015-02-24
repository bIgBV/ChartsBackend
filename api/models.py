from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

class Charts(models.Model):
    chartName =         models.CharField(max_length=200, blank=True, default='')
    description =       models.CharField(max_length=800, blank=True, default='')
    createdOn =         models.DateTimeField(auto_now_add=True, null=True)
    isPrivate =         models.BooleanField(default=False)
    jsonData =          JSONField()
    owner =             models.ForeignKey('auth.User', related_name='charts')

    def __str__(self):
        representation = self.chartName
        return representation

    class Meta:
        ordering = ('createdOn',)
