from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
# from rest_framework.authtoken.models import Token


# Overriding the default class
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'