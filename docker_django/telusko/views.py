from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import *
from rest_framework import status

def hello(request):
    return HttpResponse("Hello World");


class UserList(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, id):
        return get_object_or_404(User, pk=id)

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

