from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model, login
from django.shortcuts import render

from .models import Report
from .serializers import ReportSerializer, UserSerializer

User = get_user_model()
# Create your views here.
class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication, ]
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
