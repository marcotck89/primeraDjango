from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        User.objects.create_user('text', 'test@asd.com', 'test1')

    def test_profile_exist(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)