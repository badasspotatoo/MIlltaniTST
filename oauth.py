from flask import session

@oauth.tokengetter
def get_token(token='user'):
    if token =='user':
        return find_the_user_token()
    elif token == 'app':
        return find_the_app_token()
    raise RuntimeError('invalid token')