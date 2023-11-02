from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from tutorial.todo.models import Category
from tutorial.views import AdminLoginRequiredMixin
from .forms import CategoryCreateForm


class CategoryCreateView(AdminLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('site_admin:category_list')
    template_name = "site_admin/category/create.html"
    success_message = "登録しました。"


class CategoryListView(AdminLoginRequiredMixin, ListView):
    model = Category
    template_name = "site_admin/category/list.html"
    context_object_name = "category_list"
    paginate_by = 10
