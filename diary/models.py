from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import calendar

# Create your models here.

class DaysOfTheWeek(models.Model):
	day = models.CharField(max_length=50)

	def __str__(self):
		return self.day

class Task(models.Model):
	# day_options = calendar.weekdays()

	title = models.CharField(max_length=100)
	task_desc = models.TextField()
	day_of_task=models.ForeignKey(DaysOfTheWeek, null=True, on_delete=models.SET_NULL)
	section = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('diary')

class TodaysTask(models.Model):
	task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
	task_completed_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	date_created = models.DateField(default=timezone.now)
	date_completed = models.DateTimeField(null=True)

	def __str__(self):
		return self.task.title

	def get_absolute_url(self):
		return reverse('diary')

class AdhockTask(models.Model):

	title = models.CharField(max_length=100)
	desc = models.TextField()
	section = models.CharField(max_length=50)
	created_by = models.CharField(max_length=20)
	date_created = models.DateField(default=timezone.now)
	completed_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	date_completed = models.DateTimeField(null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('diary')
