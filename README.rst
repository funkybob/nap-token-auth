Nap Token Auth
==============

Simple Token-based authentication.

Overview
--------

A lot of people talk about having Token Auth for their REST APIs... but what does it actually mean?  And what benefit is it?

The token is cryptographically signed chunk of data.  In this case it contains the user ID, backend, and a timestamp of when it was issued.

This lets you generate and issue tokens to phone apps, services, etc, and not have to deal with logins, passwords, CSRF, etc.

Install
-------

Add to settings.MIDDLEWARE, after the default authentication
middleware:

.. code-block:: python

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'nap_token.middleware.NapTokenMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'cloudselect.middleware.CORSDefeat',
    ]


Usage
-----

When you want to log in a user, call `nap_token.get_auth_token(user)`, passing
a User instance returned from `django.contrib.auth.authenticate`.

It will return a signed, timestamped token.  The client need only pass this in
a ``Authorization`` header, formatted as 'Bearer {token}', for the request to
act as that user.  If the token is absent, expired, or invalid, `requset.user`
will fall back to the normal Session Based Auth.


Issuing Tokens
--------------

As a quick and dirty example of how to issue tokens, here's an approach that
will issue a token for a user who can log in:

.. code-block:: python

    from django.http import HttpResponse
    from django.contrib.auth.views import LoginView

    from nap_token import get_auth_token

    class TokenView(LoginView):

        def form_valid(self, form):
            user = form.get_user()
            return HttpResponse(get_auth_token(user))

