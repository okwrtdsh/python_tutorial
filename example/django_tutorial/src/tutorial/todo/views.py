from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from tutorial.views import LoginRequiredMixin
from .models import ToDoUser, ToDo
from .forms import ToDoUserCreateForm, ToDoCreateForm, ToDoEditForm


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


class ToDoDetailView(LoginRequiredMixin, DetailView):
    model = ToDo
    pk_url_kwarg = "todo_id"
    template_name = "todo/detail.html"


class ToDoEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ToDo
    form_class = ToDoEditForm
    pk_url_kwarg = "todo_id"
    template_name = "todo/edit.html"
    success_message = "修正しました。"

    def get_success_url(self):
        return reverse_lazy('todo:detail', args=(self.object.id,))
