from django.shortcuts import render
from diary.gen_todays_tasks import generate_todays_task_table
from diary.models import TodaysTask, Task, AdhockTask
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView, 
	UpdateView, 
	DeleteView
	)

# Create your views here.
# def diary(request):
# 	return render(request, 'diary/diary.html')


class DiaryListView(LoginRequiredMixin, ListView):
	
	model = TodaysTask
	template_name = 'diary/diary.html'
	context_object_name = 'task'

	def get_context_data(self, **kwarks):

		context = super(DiaryListView, self).get_context_data(**kwarks)
		context.update({
			'adhocktask':AdhockTask.objects.all(),
			})
		return context
	
	def get_queryset(self):
		return TodaysTask.objects.all()

class DiaryUpdateView(LoginRequiredMixin, UpdateView):
	model = TodaysTask
	fields = ['task', 'task_completed_by', 'date_completed']


	def get_initial(self):
		# call super if needed
		return {'task_completed_by': self.request.user, 'date_completed': datetime.datetime.now()}

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class AdhockTaskCreateView(LoginRequiredMixin, CreateView):
	model = AdhockTask
	fields = ['title', 'desc', 'section', 'created_by']

	def get_initial(self):
		# call super if needed
		return {'created_by': self.request.user}


class DiaryDetailView(LoginRequiredMixin, DetailView):
	model = TodaysTask

def diary_reset(request):

	generate_todays_task_table()
	response = redirect('/diary/')
	return response


def hard_reset(request):
	TodaysTask.objects.all().delete()
	generate_todays_task_table()

	response = redirect('/diary/')
	return response


