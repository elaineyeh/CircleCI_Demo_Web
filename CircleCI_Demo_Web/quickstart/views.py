from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import permissions, mixins, generics, viewsets
from rest_framework.generics import CreateAPIView

from quickstart.serializers import UserSerializer


def home_view(request, **kwargs):
    return HttpResponse("CICD Demo", status=200)


class RegisterAPIView(CreateAPIView):
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class RegisterMixin(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer