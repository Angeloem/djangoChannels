from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.serializers import ModelSerializer

from chat.models import Chat


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


class ChatSerializer(ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


class ChatView(ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
