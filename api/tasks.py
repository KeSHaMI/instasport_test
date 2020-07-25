from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from django.utils.timezone import now

from .models import Workout

@periodic_task(run_every=(crontab(minute='*/30')), name='clean_workouts')
def clean_workouts():

	workouts = Workout.objects.all()

	for workout in workouts:
		if workout.time < now():
			workout.delete()