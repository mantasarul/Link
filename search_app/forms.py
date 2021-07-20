from django.forms import fields
from search_app.models import Index
from django import forms


class IndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = '__all__'
        labels = {
            'title': 'Title',
            'link': 'Links',
        }


"""
class IndexForm(forms.Form):
    title = forms.CharField(max_length= 150)
    link = forms.CharField(max_length=250)
"""

