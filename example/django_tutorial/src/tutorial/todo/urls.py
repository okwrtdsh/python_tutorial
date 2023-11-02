from django.urls import path

from .views import (
    ToDoCreateView, ToDoDetailView, ToDoEditView, ToDoListView,
    ToDoUserCreateView,
)

urlpatterns = [
    path("", ToDoListView.as_view(), name="list"),
    path("<int:todo_id>/", ToDoDetailView.as_view(), name="detail"),
    path("<int:todo_id>/edit/", ToDoEditView.as_view(), name="edit"),
    path("create/", ToDoCreateView.as_view(), name="create"),
    path("user/create/", ToDoUserCreateView.as_view(), name="user_create"),
]
