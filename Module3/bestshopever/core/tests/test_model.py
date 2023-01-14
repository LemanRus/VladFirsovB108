import datetime
import sys

from django.core.exceptions import ValidationError
from django.test import TestCase
from core.models import CustomUser

sys.path.append('../')


class TestUserModels(TestCase):
    def setUp(self):
        self.user = CustomUser(
            username='test_user',
            password='testTEST1234',
            birth_date=datetime.datetime.now() + datetime.timedelta(days=1),
            email='test@test.com',
            photo='',
            secret_answer='test'
        )
        self.user.save()
        super().setUp()

    def test_birth_date(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def test_rating_calc_exists(self):
        self.assertTrue(type(self.user.rating_calc) == int)

