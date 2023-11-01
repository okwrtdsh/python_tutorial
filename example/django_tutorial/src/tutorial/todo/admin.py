from django.contrib import admin
from .models import Category, ToDoUser, ToDo

admin.site.register(Category)
admin.site.register(ToDoUser)
admin.site.register(ToDo)
