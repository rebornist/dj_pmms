from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from core import managers as core_managers

class User(AbstractUser):

	""" Custom User Model """

	GENDER_MALE = 'male'
	GENDER_FEMALE = 'female'

	GENDER_CHOICES = (
		(GENDER_MALE, _('Male')),
		(GENDER_FEMALE, _('Female')),
	)
 
	avatar = models.ImageField(null=True, blank=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=20, null=False, blank=False, default=GENDER_MALE)
	objects = core_managers.CustomUserManager()
