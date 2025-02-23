from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("todo-remove/<int:id>/", views.todo_delete, name="todo_delete"),
    path("todo-add/", views.todo_create, name="todo_create"),
    path("todo-edit/<int:id>/", views.todo_update, name="todo_update"), 
]


