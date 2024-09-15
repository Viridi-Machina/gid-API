from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from .models import Epic, Task

# Epic List View Testing ----------------------------------------------------|
class EpicListViewTest(APITestCase):
    """
    List-view tests to confirm that:
    [1] - A logged-in user can view the list of epics
    [2] - A logged-in user can create an epic
    [3] - A user not logegd-in cannot create a post
    """
    # Setup - created a user called tom
    def setUp(self):
        User.objects.create_user(username='tom', password='pass')

    # [1]
    def test_can_list_epics(self):
        tom = User.objects.get(username='tom')
        Epic.objects.create(created_by=tom, title='a title')
        response = self.client.get('/epics/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # [2] 
    def test_logged_in_user_can_create_epic(self):
        self.client.login(username='tom', password='pass')
        response = self.client.post('/epics/', {'title': 'a title'})
        count = Epic.objects.count()
        self.assertEqual(count, 1) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # [3]
    def test_user_not_logged_in_cant_create_epic(self):
        response = self.client.post('/epics/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# Epic Detail View Testing --------------------------------------------------|
class EpicDetailViewTest(APITestCase):
    """
    Detail-view tests to confirm that:
    [1] - A user can retrieve a specific epic by id
    [2] - A user cannot retrieve an epic by incorrect id
    [3] - A logged-in user can update their own epic
    [4] - A logged-in user cannot update another user's epic
    [5] - A logged-in user can delete their own epic
    [6] - A logged-in user cannot delete another user's epic
    [7] - A user not logged in cannot update or delete an epic
    """
    # Setup - create two users; tom and jerry, each with their own epics
    def setUp(self):
        tom = User.objects.create_user(username='tom', password='pass')
        Epic.objects.create(
            created_by = tom, title='a title', status='TODO'
        )
        jerry = User.objects.create_user(username='jerry', password='pass')
        Epic.objects.create(
            created_by = jerry, title='a title', status='IPRO'
        )

    # [1]
    def test_can_retrieve_epic_using_epic_id(self):
        response = self.client.get('/epics/2/')
        self.assertEqual(response.data['status'], 'IPRO')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # [2]
    def test_cant_retrieve_epic_using_invalid_id(self):
        response = self.client.get('/epics/20/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # [3]
    def test_user_can_update_own_epic(self):
        self.client.login(username='tom', password='pass')
        response = self.client.put('/epics/1/', {'title': 'a new title'})
        epic = Epic.objects.filter(pk=1).first()
        self.assertEqual(epic.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # [4]
    def test_user_cant_update_another_users_epic(self):
        self.client.login(username='tom', password='pass')
        response = self.client.put('/epics/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # [5]
    def test_user_can_delete_own_epic(self):
        self.client.login(username='tom', password='pass')
        response = self.client.delete('/epics/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # [6]
    def test_user_cannot_delete_another_users_epic(self):
        self.client.login(username='jerry', password='pass')
        response = self.client.delete('/epics/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # [7]
    def test_user_cannot_access_crud_without_login(self):
        response = self.client.delete('/epics/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.put('/epics/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
# Task List View Testing ----------------------------------------------------|
class TaskListViewTest(APITestCase)

# Task Detail View Testing --------------------------------------------------|