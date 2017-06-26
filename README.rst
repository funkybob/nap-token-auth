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

Add to settings.MIDDLEWARE_CLASSES, after the default authentication
middleware:

.. code-block:: python
   :emphasize-lines: 7

   MIDDLEWARE_CLASSES = (
      'django.contrib.sessions.middleware.SessionMiddleware',
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
      'nap_token.middleware.NapTokenMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
      'django.middleware.security.SecurityMiddleware',
   )

Usage
-----

When you want to log in a user, call `nap_token.get_auth_token(user)`, passing
a User instance returned from `django.contrib.auth.authenticate`.

It will return a signed, timestamped token.  The client need only pass this in
a ``Authorization`` header, formatted as 'Bearer {token}', for the request to
act as that user.  If the token is absent, expired, or invalid, `requset.user`
will fall back to the normal Session Based Auth.
