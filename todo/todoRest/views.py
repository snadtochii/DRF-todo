from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, authentication

from .models import Todo, User
from .serializers import TodoSerializer, UserSerializer


class TodoListView(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        todo = request.data
        serializer = TodoSerializer(data=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetailsView(APIView):

    def get_todo(self, pk):
        try:
            return Todo.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        todo = self.get_todo(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        new_todo = request.data
        old_todo = self.get_todo(pk)

        serializer = TodoSerializer(old_todo, data=new_todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        todo = self.get_todo(pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersListView(APIView):

    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsView(APIView):

    def get_user(self, pk):
        try:
            return User.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        todo = self.get_user(pk)
        serializer = UserSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        new_user = request.data
        old_user = self.get_user(pk)

        serializer = UserSerializer(old_user, data=new_user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _, pk):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
