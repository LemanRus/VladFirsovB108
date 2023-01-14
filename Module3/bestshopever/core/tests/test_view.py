import datetime
import sys
from unittest import expectedFailure

from django.test import TestCase
from core.models import CustomUser
from django.urls import reverse

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
        self.user.save()
        super().setUp()

    def test_index_without_login(self):
        response = self.client.get(reverse('ads:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Зарегистрироваться')
        self.assertContains(response, 'Войти')

    def test_index_with_login(self):
        self.client.login(username='test_user', password='testTEST1234')
        response = self.client.get(reverse('ads:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мой профиль')
        self.assertContains(response, 'Выйти')

    def test_edit_foreign_profile(self):
        self.client.force_login(CustomUser.objects.get_or_create(username='burglar')[0])
        response = self.client.get(reverse('core:profile_edit', kwargs={'user_id': self.user.pk}))
        self.assertEqual(response.status_code, 404)

    def test_password_reset_redirect(self):
        """
        Just emulate real user's actions
        """

        response = self.client.get(reverse('core:password_reset'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('core:password_reset'), {'email_for_reset': 'test@test.com'}, follow=True)
        self.assertContains(response, 'Name of your first pet')

    @expectedFailure
    def test_password_reset_unregistered_email(self):
        response = self.client.get(reverse('core:password_reset'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('core:password_reset'), {'email_for_reset': 'burglar@test.com'}, follow=True)
        self.assertContains(response, 'Name of your first pet')