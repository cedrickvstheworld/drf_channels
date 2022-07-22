from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your views here.

class IndexView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
      'chat',
      {
        "type": "notify",
        "message": 'sample ws message from API view',
      }
    )
    return Response({"message": 'Hi sucker'}, status=status.HTTP_200_OK)