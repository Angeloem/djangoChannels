from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'id',
            'first_name',
            'last_name',
            'email'
        ]


class ListCreateUsers(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUsersDelete(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer
