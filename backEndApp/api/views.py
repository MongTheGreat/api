from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import FormSerializer,UserSerializer,SchoolClassSerializer
from .models import Form,User,Class

class FormViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class SchoolClassViewSet(viewsets.ModelViewSet):

    queryset = Class.objects.all()
    serializer_class = SchoolClassSerializer
