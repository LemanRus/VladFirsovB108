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

    def test_edit_foreign_ad(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='burglar')[0])
        with self.assertRaises(Exception):
            response = self.client.get(reverse('ads:ad_edit', kwargs={'ad_id': self.ad.pk}))
