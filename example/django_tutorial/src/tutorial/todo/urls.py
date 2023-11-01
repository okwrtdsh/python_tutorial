from django.urls import path
from .views import ToDoUserCreateView

urlpatterns = [
    path("user/create/", ToDoUserCreateView.as_view(), name="user_create"),
]
