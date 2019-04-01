def get_oauth_tokens(user):
    token = user.social_auth.get(
        provider='twitter'
    ).extra_data.get('access_token')

    return token.get('oauth_token'), token.get('oauth_token_secret')