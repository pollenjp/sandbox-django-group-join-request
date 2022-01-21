# Third Party Library
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin


class AccountAdapter(DefaultAccountAdapter):
    """
    ref: <https://django-allauth.readthedocs.io/en/latest/advanced.html>
    """

    def is_open_for_signup(self, request):
        return False


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    ref: <https://django-allauth.readthedocs.io/en/latest/advanced.html>
    """

    def is_open_for_signup(self, request, socialaccount):
        return True

    def pre_social_login(self, request, sociallogin: SocialLogin):
        # sociallogin.user: User Model
        auth_user_username: str = sociallogin.user.username
        # sociallogin.account: SocialAccount
        social_account_username: str = sociallogin.account.get_provider().extract_common_fields(
            sociallogin.account.extra_data
        )["username"]
        if auth_user_username != social_account_username:
            sociallogin.user.username = social_account_username
            sociallogin.user.save()
