from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User

# class UserListCreateAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

@api_view(["GET"])
def getData(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)