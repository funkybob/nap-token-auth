Nap Token Auth
==============

Simple Token-based authentication.

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
a ``X-Auth-Token`` header for the request to act as that user.  If the token is
absent, expired, or invalid, `requset.user` will fall back to the normal
Session Based Auth.
