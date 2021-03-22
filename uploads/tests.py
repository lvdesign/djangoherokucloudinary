from django.test import TestCase
from django.urls import reverse # new
from django.contrib.auth import get_user_model
from .models import Upload


# Create your tests here.
class UploadModelTest(TestCase):

    def setUp(self):
        Upload.objects.create(title='toto')

    def test_text_content(self):
        upload= Upload.objects.get(id=1)
        expected_object_name = f'{upload.title}'
        self.assertEqual(expected_object_name, 'toto')


class HomePageViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.upload = Upload.objects.create(
            title='toto new test',
            body='Nice body content',
            author=self.user,
            )

'''
    def test_string_representation(self):
        upload = Upload(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
    
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/home')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

        '''