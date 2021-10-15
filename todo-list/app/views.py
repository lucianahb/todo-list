from rest_framework import viewsets

from models import User, Activity
from serializers import UserSerializer, ActivitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("name")
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by("status")
    serializer_class = ActivitySerializer
