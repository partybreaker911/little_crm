from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileService:
    @staticmethod
    def get_user_info(user_id):
        profile = User.objects.get(id=user_id)
        return profile
