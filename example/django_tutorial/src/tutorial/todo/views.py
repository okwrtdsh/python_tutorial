from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import ToDoUser
from .forms import ToDoUserCreateForm


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
