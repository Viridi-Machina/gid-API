from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from .models import Epic, Task


class EpicListViewTest(APITestCase):
    """
    View tests to confirm that:
    - A logged-in user can view the list of epics
    - A logged-in user can create an epic
    - A user not logegd-in cannot create a post
    """
    def setUp(self):
        User.objects.create_user(username='tom', password='pass')

    def test_can_list_epics(self):
        tom = User.objects.get(username='tom')
        Epic.objects.create(created_by=tom, title='a title')
        response = self.client.get('/epics/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_epic(self):
        self.client.login(username='tom', password='pass')
        response = self.client.post('/epics/', {'title': 'a title'})
        count = Epic.objects.count()
        self.assertEqual(count, 1) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_epic(self):
        response = self.client.post('/epics/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)