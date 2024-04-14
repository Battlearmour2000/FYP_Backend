from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import check_password
from rest_framework import status
import hashlib


def hash_password(password):
    password_bytes=password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    hex_dig = hash_object.hexdigest()
    
    return hex_dig

@api_view(["GET"])
def get_user(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    
    #check if data is valid
    if serializer.is_valid():
        # get the raw pssword
        unhashed_password = request.data.get('password', None)
        # hash the password
        hashed_password = hash_password(unhashed_password)
        # save the hasded password into model
        serializer.validated_data['password'] = hashed_password
        serializer.save()
        
        #return data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # return error if data is invalid
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST'])
def login(request):
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    
    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'email doesnt exist'}, status=status.HTTP_401_UNAUTHORIZED)

    hashed_password = hash_password(password)  # Hash the provided password
    if hashed_password != user.password:  # Compare the hashed password with the stored hashed password
        hash_str = str(hashed_password)
        return Response({'error': 'Invalid credentials', 'password': hash_str}, status=status.HTTP_401_UNAUTHORIZED)

    serializer = UserSerializer(user)
    return Response(serializer.data)