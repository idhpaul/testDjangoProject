from django.conf import settings
from django.contrib.auth.backends import BaseBackend


class AuthenticationWithoutPassword(BaseBackend):

    def authenticate(self, request, username=None):
        if username is None:
            username = request.data.get('username', '')
        try:
            return settings.AUTH_USER_MODEL.objects.get(username=username)
        except settings.AUTH_USER_MODEL.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return settings.AUTH_USER_MODEL.objects.get(pk=user_id)
        except settings.AUTH_USER_MODEL.DoesNotExist:
            return None