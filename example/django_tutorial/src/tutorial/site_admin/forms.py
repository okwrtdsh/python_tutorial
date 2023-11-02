from django import forms

from tutorial.forms import FormControlMixin
from tutorial.todo.models import Category


class CategoryCreateForm(forms.ModelForm, FormControlMixin):

    class Meta:
        model = Category
        fields = [
            'order',
            'name',
        ]


class CategoryEditForm(forms.ModelForm, FormControlMixin):

    class Meta:
        model = Category
        fields = [
            'enabled',
            'order',
            'name',
        ]
