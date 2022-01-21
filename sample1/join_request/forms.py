# Third Party Library
from django import forms

# Local Library
from .models import RequestPost


class RequestPostForm(forms.ModelForm):
    class Meta:
        model = RequestPost
        fields = ("request_group", "detail")
