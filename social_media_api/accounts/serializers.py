from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username','email','password','bio','token']

    def get_token9(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key

class UserProfileSerializer(serializers.ModelSerializer):
    following_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        fields = ['username','email','bio','profile_picture','followers_count','following_count']

    def get_following_count(self, obj):
        return obj.following.count()

    def get_followers_count(self, obj):
        return obj.followers.count()
