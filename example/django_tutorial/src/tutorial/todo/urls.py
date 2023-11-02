from django.urls import path
from .views import ToDoUserCreateView, ToDoCreateView, ToDoListView, ToDoDetailView

urlpatterns = [
    path("", ToDoListView.as_view(), name="list"),
    path("<int:todo_id>/", ToDoDetailView.as_view(), name="detail"),
    path("create/", ToDoCreateView.as_view(), name="create"),
    path("user/create/", ToDoUserCreateView.as_view(), name="user_create"),
]
