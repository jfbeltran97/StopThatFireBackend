from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Report, UserProfile, Location

User = get_user_model()

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('lat', 'lng')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        print(validated_data)
        password = validated_data.pop('password')
        phone = validated_data.pop('phone', None)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        if phone:
            UserProfile.objects.create(user=user, phone=phone)
        return user


class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    location = LocationSerializer()

    class Meta:
        model = Report
        fields = ('description', 'image', 'user', 'location')

    def create(self, validated_data):
        location_dict = validated_data.pop('location')
        location_obj = Location.objects.create(**location_dict)
        report = Report.objects.create(**validated_data, location=location_obj)
        return report
