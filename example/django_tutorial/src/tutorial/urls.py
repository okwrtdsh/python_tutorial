from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import include, path

urlpatterns = [
    path("", lambda request: render(request, "index.html"), name="index"),
    path("todo/", include(("tutorial.todo.urls", "todo"), namespace="todo")),
    path("admin/", include(("tutorial.site_admin.urls", "site_admin"), namespace="site_admin")),
    path("admin/native/", admin.site.urls),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="index"), name="logout"),
]
