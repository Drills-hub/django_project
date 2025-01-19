# tests.py
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status


User = get_user_model()

@pytest.mark.django_db
class TestLoginAPIView:

#테스트 유저 생성
    @pytest.fixture
    def create_user(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        return user

#로그인 성공 테스트
    def test_login_success(self, client, create_user):
        url = reverse('login')  
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        response = client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'token' in response.data
        assert response.data['token'] is not None

#로그인 실패 테스트
    def test_login_invalid_credentials(self, client):
        url = reverse('login')  
        data = {
            'username': 'invaliduser',
            'password': 'invalidpassword'
        }

        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['message'] == "아이디 또는 비밀번호를 잘못 입력했습니다."
