from rest_framework.authentication import TokenAuthentication as AuthenticationClass


class TokenAuthentication(AuthenticationClass):
    keyword = "Bearer"

