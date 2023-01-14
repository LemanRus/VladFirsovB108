import datetime
import sys
from unittest import expectedFailure

from django.test import TestCase
from django.urls import reverse

from core.models import CustomUser
from ads.models import Advertisement

sys.path.append('../')


class TestView(TestCase):
    def setUp(self):
        self.user = CustomUser(
            username='test_user',
            birth_date=datetime.datetime.now() - datetime.timedelta(days=100),
            email='test@test.com',
            photo='',
            secret_answer='test'
        )
        self.user.set_password('testTEST1234')

        self.ad = Advertisement(
            author=self.user,
            title='TestAd',
            description='Test Description',
        )

        self.user.save()
        self.ad.save()
        super().setUp()

    def test_create_ability_as_default(self):
        self.ad.full_clean()
        self.assertEqual(self.ad.category.title, 'Common')