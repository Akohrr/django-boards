from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board, Post, Topic
from ..views import topic_posts, PostListView


class TopicPostsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Django Board.', description='A django boards application')
        user = User.objects.create(username='John', email='john@doe.com')
        topic = Topic.objects.create(subject='Test topic', board=board, starter=user)
        self.url = reverse('topic_posts', kwargs={'pk':board.pk, 'topic_pk':topic.pk})
        self.response = self.client.get(self.url)

    def test_topic_posts_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        # view = resolve('/boards/1/topics/1/')
        view = resolve(self.url)
        self.assertEquals(view.func.view_class, PostListView)
