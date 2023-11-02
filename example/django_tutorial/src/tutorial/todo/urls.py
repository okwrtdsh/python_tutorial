from django.urls import path
from .views import ToDoUserCreateView, ToDoCreateView, ToDoListView

urlpatterns = [
    path("", ToDoListView.as_view(), name="list"),
    path("create/", ToDoCreateView.as_view(), name="create"),
    path("user/create/", ToDoUserCreateView.as_view(), name="user_create"),
]
