from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from tutorial.views import LoginRequiredMixin
from .models import ToDoUser, ToDo
from .forms import ToDoUserCreateForm, ToDoCreateForm


class ToDoUserCreateView(SuccessMessageMixin, CreateView):
    model = ToDoUser
    form_class = ToDoUserCreateForm
    success_url = reverse_lazy('index')
    template_name = "todo/user_create.html"
    success_message = "登録しました。"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs


class ToDoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ToDo
    form_class = ToDoCreateForm
    success_url = reverse_lazy('todo:list')
    template_name = "todo/create.html"
    success_message = "登録しました。"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs


class ToDoListView(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = "todo/list.html"
    context_object_name = "todo_list"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user__id=self.request.user.id)
        return queryset
