from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import User, Idea, Comment

class ProjectSparkAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword',
        )
        # Create a test idea
        self.idea = Idea.objects.create(
            title='Test Idea',
            description='This is a test idea',
            # tags = ['tag1', 'tag2'],
            created_by=self.user
        )

        # Create a test comment
        self.comment = Comment.objects.create(
            idea=self.idea,
            commenter=self.user,
            content='This is a test comment'
        )
    def test_create_idea(self):
        url = reverse('idea-list')
        response = self.client.post(url, args=[self.idea.id])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_idea_list(self):
        url = reverse('idea-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_idea_detail(self):
        url = reverse('idea-detail', args=[self.idea.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Idea')

    def test_comment_create(self):
        url = reverse('comment-create', args=[self.idea.id])
        data = {
            'idea': self.idea.id,
            'content': 'New comment',
            'commenter': self.user.id
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_comment_list(self):
        url = reverse('comment-create', args=[self.idea.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['content'], 'This is a test comment')

    def test_comment_delete(self):
        url = reverse('comment-detail', args=[self.idea.id, self.comment.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)


 