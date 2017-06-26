from django.conf import settings
from django.contrib.auth import load_backend
from django.contrib.auth.models import AnonymousUser
from django.core import signing
from django.utils.functional import SimpleLazyObject


def get_user(token, user):
    if token:
        try:
            user_id, backend_path = signing.loads(token, salt='nap_token.auth', max_age=settings.SESSION_COOKIE_AGE)
        except signing.SignatureExpired:
            # Quietly show they're logged out
            pass
        except signing.BadSignature:
            # Noisily show they're dodgy
            pass
        else:
            if backend_path in settings.AUTHENTICATION_BACKENDS:
                backend = load_backend(backend_path)
                user = backend.get_user(user_id)
    return user or AnonymousUser()


class NapTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '')
        if token.startswith('Bearer '):
            token = token.split(' ', 1)[1].strip()
            original_user = getattr(request, 'user')
            request.user = SimpleLazyObject(lambda: get_user(token, original_user))
        return self.get_response(request)
