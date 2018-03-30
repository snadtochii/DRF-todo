from rest_framework import serializers

from .models import Todo, User


# class SignUpUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', )


class UserPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')


class TodoSerializer(serializers.ModelSerializer):
    users = UserPreviewSerializer(many=True)

    class Meta:
        model = Todo
        fields = '__all__'
