from django.contrib.auth.hashers import is_password_usable, make_password
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Request(models.Model):
    class Status(models.TextChoices):
        STAND_BY = 'SB', _('Stand-by')
        PROCESSING = 'PR', _('Processing')
        FINISH = 'FN', _('Finish')
        ERROR = 'ER', _('Error')
        DELETE_USER = 'DU', _('Deleted by User')
        EXPIRED = 'EX', _('Expired')

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=10)
    password = models.CharField(max_length=30)
    content = models.TextField(max_length=300)  # TODO: replace with photo
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.STAND_BY
    )
    reg_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(blank=True, null=True)



@receiver(pre_save, sender=Request)
def password_hashing(instance, **kwargs):
    if not is_password_usable(instance.password):
        instance.password = make_password(instance.password)
