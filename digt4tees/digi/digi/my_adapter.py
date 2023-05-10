from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

#from allauth.account.models import EmailAddress
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.http import HttpResponse
from django.contrib import auth



class MyAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):

        # social account already exists, so this is just a login
        if sociallogin.is_existing:
            return

        # some social logins don't have an email address
        if not sociallogin.email_addresses:
            return

        # find the first verified email that we get from this sociallogin
        verified_email = None
        for email in sociallogin.email_addresses:
            if email.verified:
                verified_email = email
                break

        # no verified emails found, nothing more to do
        if not verified_email:
            return

        # check if given email address already exists as a verified email on
        # an existing user's account
        try:
            existing_email = User.objects.get(email__iexact=email.email)
        except User.DoesNotExist:
            return

        # if it does, connect this new social login to the existing user
        sociallogin.connect(request, existing_email)


 