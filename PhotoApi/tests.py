from django.test import TestCase, TransactionTestCase, Client
from django.contrib.auth.models import User
from io import StringIO
from PIL import Image
from django.core.files.base import File
import tempfile
import json


class PhotoTestCase(TransactionTestCase, Client):

    def setUp(self):
        user1 = User(username="user1")
        user1.set_password('password123')
        user1.save()
        user2 = User(username="user2")
        user2.set_password('password123')
        user2.save()
        self.photo_id = None
        self.auth_token = None

    def create_fake_image(self):
        """
        Util method to create fake image file
        """
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            image = Image.new('RGB', (200, 200), 'white')
            image.save(f, 'PNG')

        return open(f.name, mode='rb')

    def auth_test(self, username, password):
        """
        Testcase to authenticate with valid credentials
        """
        url = '/authenticate/'
        data = {'username': username, 'password': password}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.auth_token = 'JWT {}'.format(response.json()['token'])
        # self.client.defaults['HTTP_AUTHORIZATION'] = self.auth_token

    def getPhotosList_test(self):
        """
        Testcase to check photos list endpoint
        """
        url = '/photos/'
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 200)

    def retrievePhoto_test(self):
        """
        Testcase to check retrieve photo endpoint
        """
        url = '/photos/{}/'.format(self.photo_id)
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)

    def addPhoto_without_authorization_test(self):
        """
        Test case to try to add photo without authentication
        """
        url = '/photos/add/'
        data = {
            'photo': self.create_fake_image()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 401)

    def addPhoto_with_authorization_test(self):
        """
        Test case to try to add photo without authentication
        """
        url = '/photos/add/'
        data = {
            'photo': self.create_fake_image()
        }
        response = self.client.post(url, data, HTTP_AUTHORIZATION=self.auth_token)
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.content)
        self.photo_id = response_data['id']

    def deletePhoto_test(self, isOwner=False):
        """
        Test case to check delete photo endpoint
        """
        url = '/photos/delete/{}/'.format(self.photo_id)
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.auth_token)
        if isOwner:
            self.assertEqual(response.status_code, 204)
        else:
            self.assertEqual(response.status_code, 403)

    def test_flow(self):
        self.getPhotosList_test()
        self.addPhoto_without_authorization_test()
        self.auth_test(username="user1", password="password123")
        self.addPhoto_with_authorization_test()
        self.retrievePhoto_test()
        self.auth_test(username="user2", password="password123")
        self.deletePhoto_test(isOwner=False)
        self.auth_test(username="user1", password="password123")
        self.deletePhoto_test(isOwner=True)
