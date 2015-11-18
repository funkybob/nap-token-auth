from django.core import signing


def get_auth_token(user):
    '''
    Generate a token for a user.
    '''
    return signing.dumps((user.pk, user.backend), salt='nap_token.auth')
