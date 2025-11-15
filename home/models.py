# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    cuit = models.CharField(max_length=255, null=True, blank=True)
    legajo = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Ejemplo(models.Model):

    #__Ejemplo_FIELDS__
    campo1 = models.CharField(max_length=255, null=True, blank=True)
    campo2 = models.IntegerField(null=True, blank=True)

    #__Ejemplo_FIELDS__END

    class Meta:
        verbose_name        = _("Ejemplo")
        verbose_name_plural = _("Ejemplo")



#__MODELS__END
