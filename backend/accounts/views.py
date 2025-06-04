from accounts import models, serializers
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]


class UserShiftViewset(viewsets.ModelViewSet):
    queryset = models.UserShift.objects.all()
    serializer_class = serializers.UserShiftSerializer
    permission_classes = [permissions.AllowAny]
