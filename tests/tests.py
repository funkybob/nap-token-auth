from django.contrib import auth
from django.core.signing import b64_encode
from django.test import TestCase

from nap_token import get_auth_token


CREDENTIALS = {
    'username': 'test',
    'password': 'abc123',
}

class TokenTest(TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a superuser for testing
        from django.contrib.auth.models import User
        u = User.objects.create_superuser(email='user@super.com', **CREDENTIALS)
        super(TokenTest, cls).setUpClass()

    def test_unauth(self):
        resp = self.client.get('/admin/')
        self.assertRedirects(resp, '/admin/login/?next=/admin/')

    def test_normal_login(self):
        self.client.login(**CREDENTIALS)
        resp = self.client.get('/admin/')
        self.assertEqual(resp.status_code, 200)

    def test_token_auth(self):
        u = auth.authenticate(**CREDENTIALS)
        t = get_auth_token(u)

        resp = self.client.get('/admin/', HTTP_X_AUTH_TOKEN=t)
        self.assertEqual(resp.status_code, 200)

    def test_both_auth(self):
        self.client.login(**CREDENTIALS)

        u = auth.authenticate(**CREDENTIALS)
        t = get_auth_token(u)

        resp = self.client.get('/admin/', HTTP_X_AUTH_TOKEN=t)
        self.assertEqual(resp.status_code, 200)

    def test_bogus(self):
        t = b64_encode(b'random')

        resp = self.client.get('/admin/', HTTP_X_AUTH_TOKEN=t)
        self.assertRedirects(resp, '/admin/login/?next=/admin/')

    def test_expired(self):
        u = auth.authenticate(**CREDENTIALS)
        t = get_auth_token(u)

        with self.settings(SESSION_COOKIE_AGE=0):
            resp = self.client.get('/admin/', HTTP_X_AUTH_TOKEN=t)
        self.assertRedirects(resp, '/admin/login/?next=/admin/')
