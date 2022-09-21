from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse
from .models import DSS, Comment, Reply, SoftwareUpdate, Deployment
from django.views.generic import (
	ListView,
	DetailView,
	CreateView, 
	UpdateView, 
	DeleteView
	)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import date
import calendar
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html


# Create your views here.
# def home(request):
# 	return render(request, 'board/home.html')



class DSSListView(LoginRequiredMixin, ListView):
	model = DSS
	template_name = 'board/home.html'
	context_object_name = 'DSS'

	def get_context_data(self, **kwarks):
		context = super(DSSListView, self).get_context_data(**kwarks)

		#used to compair today with the the day_of_weekly servicing purple box
		curr_date = date.today()
		the_day = calendar.day_name[curr_date.weekday()]

		#used to work out the column headings
		states = DSS.objects.values('servicable').distinct()
		distinct_states = []
		for x in states:
			distinct_states.append(x['servicable'])

		#used to calculate home page col-width
		states = DSS.objects.values('servicable').distinct()
		distinct_states_count = states.count()
		if distinct_states_count <= 3:
			col_width = 4
		else:
			col_width = 3

		#used to calculate the DSS tile width
		state_totals = DSS.objects.all().values('servicable').annotate(total=Count('servicable')).order_by('-total')		
		
		serviceable_totals = {}
		for x in state_totals:
			serviceable_totals[x['servicable']] = x['total']
		
		#Geographic Plot

		df = {'deployment_location':('USA','FRA','POL','ITA' ), 'num_personnel_req':(2,6,4,3 )}

		geo_data = dict(
				type = 'choropleth',
				locations = df['deployment_location'],
				z = df['num_personnel_req'],
				colorscale= 'Portland',
				colorbar = {'title' : 'Personnel per Location'},
				marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1))
				)

		geo_layout = dict(
			height=500,
			# title = 'Location of Deployed Personnel',
			title_xanchor='right',
			geo = dict(
				# showframe = True,
				projection = {'type':'robinson'}
			)
			)
		
		figure = go.Figure(data=geo_data,layout=geo_layout)

		context.update({
				'comments':Comment.objects.order_by('-date_posted')[0:3:],
				'updates':SoftwareUpdate.objects.all()[0:1:],
				'today':the_day,
				'serviceablility_headings':distinct_states,
				'column_width':col_width,
				'state_totals':serviceable_totals,
				'graph':figure.to_html,
			})
		return context
	
	def get_queryset(self):
		return DSS.objects.order_by('title')


class DSSUpdateView(LoginRequiredMixin, UpdateView):
	model = DSS
	fields = ['title', 'db_num', 'servicable', 'trilogi_version', 'wdms_version']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class CommentCreateView(CreateView):
	model = Comment
	fields = ['title', 'content']

class SoftwareUpdateView(UpdateView):
	model = SoftwareUpdate
	fields = ['trilogi_issue', 'wdms_issue', 'tdss_issue']
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class DeploymentListView(LoginRequiredMixin, ListView):
	model = Deployment
	template = 'deployment_list.html'

	def get_context_data(self, **kwarks):
		context = super(DeploymentListView, self).get_context_data(**kwarks)

		#Geographic Plot

		df = {'deployment_location':('USA','FRA','POL', ), 'num_personnel_req':(2,6,4, )}

		geo_data = dict(
				type = 'choropleth',
				locations = df['deployment_location'],
				z = df['num_personnel_req'],
				colorscale= 'Portland',
				colorbar = {'title' : 'Personnel per Location'},
				marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1))
				)

		geo_layout = dict(
			height=500,
			# title = 'Location of Deployed Personnel',
			title_xanchor='right',
			geo = dict(
				# showframe = True,
				projection = {'type':'robinson'}
			)
			)
		
		figure = go.Figure(data=geo_data,layout=geo_layout)

		context.update({
				'comments':Comment.objects.order_by('-date_posted')[0:3:],
				'graph':figure.to_html,
			})
		return context
	
	def get_queryset(self):
		return Deployment.objects.order_by('start_date')
