from . serializers import UserSerializer
from rest_framework import generics
from user . models import User

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
