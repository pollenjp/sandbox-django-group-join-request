# Standard Library
from logging import getLogger

# Third Party Library
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialLogin

logger = getLogger(__name__)


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

    def is_open_for_signup(self, request, sociallogin: SocialLogin):
        logger.debug(f"{sociallogin.account.provider=}")
        if sociallogin.account.provider == "google":
            return True
        return False
