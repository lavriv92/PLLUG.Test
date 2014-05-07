import re

from django import forms
from .models import Group


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group

    def clean(self):
        cleaned_data = super(GroupForm, self).clean()
        name = cleaned_data.get('name')
        pattern = r'[a-zA-Z]{3}[0-9]{3}'
        if not re.match(pattern=pattern, string=name):
            raise forms.ValidationError('your is looser')

        return cleaned_data
