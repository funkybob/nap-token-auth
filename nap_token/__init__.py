
def get_auth_token(user)
    '''
    Generate a token for a user.
    '''
    token = signing.dumps((user.pk, user.backend), salt='nap_token.auth')
