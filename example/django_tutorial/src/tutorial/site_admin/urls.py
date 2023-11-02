from django.urls import path
from .views import CategoryCreateView

urlpatterns = [
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
]
