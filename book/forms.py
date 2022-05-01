from django import forms
from django.forms import widgets


class GuestBookForm(forms.Form):
    name = forms.CharField(max_length=30, required=True, label="Name",
                           error_messages={"required": 'Enter data'})
    mail = forms.EmailField(max_length=40, required=True, label="Email",
                            error_messages={"required": 'Enter data'})
    post_text = forms.CharField(max_length=2000, required=True,
                                label="Your text",
                                widget=forms.widgets.Textarea(attrs={"rows": 5, "cols": 20}),
                                error_messages={"required": 'Enter data'})
