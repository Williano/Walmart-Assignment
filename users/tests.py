from unittest import mock
from django.test import SimpleTestCase
from django.urls import reverse

### python manage.py test ###


class UserTestCase(SimpleTestCase):

    @mock.patch('requests.post')
    def test_homepage_status_code(self, mock_get):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.post')
    def test_homepage_url_name(self, mock_get):
        response = self.client.get(reverse('users:home'))

        self.assertEqual(response.status_code, 200)


class PostTestCase(SimpleTestCase):

    @mock.patch('requests.post')
    def test_user_post_list_status_code(self, mock_get):
        response = self.client.get(reverse('users:user_posts', kwargs={'id': 4}))

        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.post')
    def test_user_post_list_template(self, mock_get):
        response = self.client.get(reverse('users:user_posts', kwargs={'id': 4}))

        self.assertTemplateUsed(response, 'users/user-post.html')


class AlbumTestCase(SimpleTestCase):

    @mock.patch('requests.post')
    def test_user_albums_list_status_code(self, mock_get):
        response = self.client.get(reverse('users:user_albums', kwargs={'id': 4}))

        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.post')
    def test_album_photos_template(self, mock_get):
        response = self.client.get(reverse('users:album_photos', kwargs={'id': 4}))

        self.assertTemplateUsed(response, 'users/user-album-photos.html')


class CommentTestCase(SimpleTestCase):

    @mock.patch('requests.post')
    def test_post_comments_list_status_code(self, mock_get):
        response = self.client.get(reverse('users:post_comments', kwargs={'id': 4}))

        self.assertEqual(response.status_code, 200)

    @mock.patch('requests.post')
    def test_album_photos_template(self, mock_get):
        response = self.client.get(reverse('users:post_comments', kwargs={'id': 4}))

        self.assertTemplateUsed(response, 'users/post-comment.html')
