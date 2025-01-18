from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import Role


class SignupAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            role_data = request.data.get("roles")

            if role_data:
                for role in role_data:
                    role_instance = Role.objects.get_or_create(
                        user=user, role=role["role"]
                    )[0]
                    role_instance.save()
            else:
                Role.objects.create(user=user, role="USER")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {"message": "아이디 또는 비밀번호를 잘못 입력했습니다."}, status=400
            )
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "token": str(refresh.access_token),
            }
        )
