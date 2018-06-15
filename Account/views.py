import logging

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User


# Create your views here.

class UserActivateView(TemplateView):
    logger = logging.getLogger(__name__)
    template_name = 'registration/user_activate_complete.html'

    def get(self, request, *args, **kwargs):
        self.logger.debug('UserActivateView.get()')

        uid = force_text(urlsafe_base64_decode(self.kwargs['uidb64']))
        token = self.kwargs['token']

        self.logger.debug('uid: %s, token: %s' % (uid, token))

        try:
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            self.logger.warning('User %s not found' % uid)
            user = None

        if user is not None and PasswordResetTokenGenerator().check_token(user, token):
            user.is_active = True
            user.save()
            self.logger.info('User %s(pk=%s) has been activated.' % (user, user.pk))

        return super(UserActivateView, self).get(request, *args, **kwargs)
