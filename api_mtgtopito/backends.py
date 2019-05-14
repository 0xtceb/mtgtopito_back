from django.contrib.auth.models import User


class EmailAuthenticate(object):

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            return User.objects.filter(email=username).order_by('id').first()

        if user.check_password(password):
            return user
        return None

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
