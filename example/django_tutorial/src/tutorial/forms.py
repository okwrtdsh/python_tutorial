from django import forms


class FormControlMixin(forms.BaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if not isinstance(self.fields[field].widget, (
                    forms.CheckboxInput, forms.RadioSelect)):
                self.fields[field].widget.attrs.update(
                    {'class': "form-control"})
