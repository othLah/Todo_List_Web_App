from django.urls import path
from . import views

urlpatterns = [
	path("", views.todo, name="todo_page"),
	path("add/", views.add, name="add_page"),
	path("completed/<c_id>", views.completed, name="completed_page"),
	path("delete_completed", views.delete_completed, name="delete_completed_page"),
	path("delete_all", views.delete_all, name="delete_all_page")
]	