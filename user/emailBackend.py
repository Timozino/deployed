from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackEnd(ModelBackend):
    def authenticate(self,  username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
            
        except UserModel.DoesNotExist:
            return 'ko si'
        else:
            if user.check_password(password):
               # pass
                
                return user
        return None