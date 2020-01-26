from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class UserModelTest(TestCase):
    """Test for the user model"""

    def setUp(self):
        test_user = get_user_model().objects.create(
            username='testuser', password='abcd1234')
        test_user.save()

    def test_user_info(self):
        user = get_user_model().objects.get(id=1)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'abcd1234')


class UserViewTest(APITestCase):
    """Test for the api views"""
    
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/v1/users/'
        self.wrong_url = '/api/users/'
        self.user = get_user_model().objects.create(
            username='testuser', password='abcd1234')
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_not_found(self):
        response = self.client.get(self.wrong_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_create(self):
        response = self.client.post(
            self.url,
            {'username': 'testuser1'},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_detail(self):
        response = self.client.get(f'{self.url}{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_info_update(self):
        response = self.client.put(
            f'{self.url}{self.user.pk}/',
            {'username': 'testuser1_changed'},
            format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_info_delete(self):
        response = self.client.delete(f'{self.url}{self.user.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class UserAuthTest(APITestCase):
    """Test user authentication"""

    def setUp(self):
        self.data = {
            'username': 'testuser111',
            'email': 'testuser111@email.com',
            'password1': 'testpass123',
            'password2': 'testpass123'}
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='peter',
            password='peter1234')

    def test_user_registration(self):
        response = self.client.post(
            '/api/v1/rest-auth/registration/',
            self.data,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_info(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/api/v1/rest-auth/user/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_info_update(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            "/api/v1/rest-auth/user/",
            {'username': 'peter_pen'},
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
