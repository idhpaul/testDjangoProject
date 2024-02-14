from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

UserModel = get_user_model()

class AuthenticationWithoutPassword(BaseBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = request.data.get('email')
        try:
            return UserModel.objects.filter(email=username).first()
                    
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None