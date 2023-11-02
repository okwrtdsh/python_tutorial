from django.contrib import admin

from .models import Category, ToDo, ToDoUser

admin.site.register(Category)
admin.site.register(ToDoUser)
admin.site.register(ToDo)
