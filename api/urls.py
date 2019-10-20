from rest_framework.routers import DefaultRouter
from fcm_django.api.rest_framework import FCMDeviceAuthorizedViewSet
from django.urls import path
from .views import ReportViewSet, UserViewSet, LoginView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'devices', FCMDeviceAuthorizedViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
] + router.urls
