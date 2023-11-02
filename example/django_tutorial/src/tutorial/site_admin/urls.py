from django.urls import path

from .views import CategoryCreateView, CategoryEditView, CategoryListView

urlpatterns = [
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/<int:category_id>/", CategoryEditView.as_view(), name="category_edit"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
]
