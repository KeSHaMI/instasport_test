from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.utils.timezone import now
# Create your models here.


def time_validator(time):
	"""Raises error if time less than current"""
	if time < now():
		raise ValidationError('You cannot start workout in the past!')


class User(AbstractUser):
	email = models.EmailField(max_length=255, unique=True)
	REQUIRED_FIELDS = ['password', 'username', 'is_staff', 'is_superuser']

	USERNAME_FIELD = 'email'

	def __str__(self):
		return self.username

class Workout(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
	time = models.DateTimeField(validators=[time_validator])
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name
