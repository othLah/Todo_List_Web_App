from django.shortcuts import render, redirect
from . import models, forms
from django.views.decorators.http import require_POST

def todo(request):
	plans = models.Todo_Plan.objects.order_by("id")
	todo_form_model = forms.Todo_Form_Model()
	nbre_info = models.Todo_Plan.objects.count()
	dico = {"plans_key": plans, "todo_form_key": todo_form_model, "nbre_info_key": nbre_info}
	return render(request, "todo/todo.html", dico)

@require_POST
def add(request):
	todo_r = None
	try:
		todo_r = models.Todo_Plan.objects.get(id="666")
	except:
		pass
	new_plan = forms.Todo_Form_Model(request.POST, instance=todo_r)
	if new_plan.is_valid():
		new_plan.save()
	return redirect("todo_page")

def completed(requets, c_id):
	plan_r = models.Todo_Plan.objects.filter(id__exact=c_id).get()
	plan_r.completed = True
	plan_r.save()
	return redirect("todo_page")

def delete_completed(request):
	models.Todo_Plan.objects.filter(completed__exact=True).delete()
	return redirect("todo_page")

def delete_all(request):
	models.Todo_Plan.objects.all().delete()
	return redirect("todo_page")