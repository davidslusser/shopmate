import logging

# import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)
from django.dispatch import receiver
from djangoaddicts.signalcontrol.decorators import signal_control

user_logger = logging.getLogger("user")


# log user login succeeded
@receiver(user_logged_in)
@signal_control
def log_user_login(sender, user, request, **kwargs):
    """log user login to user log"""
    user_logger.info(f"login successful for user: {user}")


# log user login failed
@receiver(user_login_failed)
# @signal_control
def log_user_login_failed(sender, user=None, **kwargs):
    """log user login to user log"""
    login_username = kwargs["credentials"].get("username", None)
    if not user and login_username:
        user = User.objects.filter(username=login_username).last()
    if user:
        user_logger.info(f"login failed for user: {user}")
    else:
        user_logger.info("login failed; unknown user")


# log user logout
@receiver(user_logged_out)
# @signal_control
def log_user_logout(sender, user, **kwargs):
    """log user logout to user log"""
    user_logger.info(f"logout successful for user: {user}")
