from django.urls import path
from .views import ToDoUserCreateView, ToDoCreateView

urlpatterns = [
    path("create/", ToDoCreateView.as_view(), name="create"),
    path("user/create/", ToDoUserCreateView.as_view(), name="user_create"),
]
