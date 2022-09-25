from operator import mod
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class DSS(models.Model):
	title = models.CharField(max_length=100)
	db_num = models.CharField(max_length=8)
	servicable = models.CharField(max_length=100)
	wdms_version = models.CharField(max_length=10)
	trilogi_version = models.CharField(max_length=10)
	day_of_weekly = models.CharField(max_length=10)
	notes = models.TextField()
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('board-home')


class Comment(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('board-home')

class Reply(models.Model):
	linked_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class SoftwareUpdate(models.Model):
	wdms_issue = models.CharField(max_length=10)
	trilogi_issue = models.CharField(max_length=10)
	tdss_issue = models.CharField(max_length=10)

	def __str__(self):
		return 'Software Update'

class Deployment(models.Model):
	location = models.CharField(max_length=100)
	location_code = models.CharField(max_length=5)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def get_absolute_url(self):
		return reverse('deployment')

class InBuild(models.Model):
	dss_in_build = models.ForeignKey(DSS, on_delete=models.CASCADE)

	def __str__(self):
		return self.dss_in_build.__dict__['title']

class BuildStages(models.Model):
	stage = models.IntegerField()
	stage_title = models.TextField()
	stage_desc = models.TextField()
	exp_comp_time = models.IntegerField()
	
	def __str__(self):
		return self.stage_title

class DatesOfBuildStages(models.Model):
	build_item = models.ForeignKey(InBuild, on_delete=models.CASCADE)
	build_stage = models.ForeignKey(BuildStages, on_delete=models.CASCADE)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.build_item.__str__()}_{self.build_stage.__dict__["stage_title"]}'