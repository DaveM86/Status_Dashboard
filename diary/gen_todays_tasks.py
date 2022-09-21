import datetime
import calendar
from diary.models import Task, DaysOfTheWeek as dotw, TodaysTask as tt


def clear_task_list():

	tt.objects.all().delete()

def get_todays_tasks():
	#used to compair today with the the day_of_weekly servicing purple box
	curr_date = datetime.date.today()
	the_day = calendar.day_name[curr_date.weekday()]

	matching_days = dotw.objects.get(day = the_day)
	all_days = dotw.objects.get(day = 'Every Day')

	tasks_to_gen = Task.objects.filter(day_of_task = matching_days)|Task.objects.filter(day_of_task = all_days)

	return (tasks_to_gen)

def generate_todays_task_table():

	test = tt.objects.all().first()

	if test == None:
		tasks = get_todays_tasks()
		for task in tasks:
			t = tt.objects.create(task = task)
			t.save()

	elif test.date_created == datetime.date.today():
		pass

	else:
		clear_task_list()
		tasks = get_todays_tasks()
		for task in tasks:
			t = tt.objects.create(task = task)
			t.save()

# def generate_todays_task_table():

# 	test = tt.objects.all().first()

# 	if test.date_created != datetime.date.today():
# 		if test != None:
# 			clear_task_list()
		
# 		tasks = get_todays_tasks()
# 		for task in tasks:
# 			t = tt.objects.create(task = task)
# 			t.save()				