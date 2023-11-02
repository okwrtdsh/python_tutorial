from django.urls import path
from .views import CategoryCreateView, CategoryListView

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
]
