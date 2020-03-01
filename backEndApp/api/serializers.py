from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Form, User,Class


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id','first_name', 'last_name', 'email', 'mobile_number']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'email']

class SchoolClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ['id', 'name', 'subject', 'code', 'teacher']

