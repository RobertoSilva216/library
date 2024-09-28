from django.db import IntegrityError
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from api.serializers import UserSerializer, UserSerializerOut


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.create_user(
                request.data['username'],
                request.data['email'],
                request.data['password'],
                **{
                    'first_name': request.data['first_name'],
                    'last_name': request.data['last_name'],
                }
            )
            if user:
                return Response(UserSerializerOut(user).data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)

