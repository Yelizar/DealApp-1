from django import forms

from .models import GoodsFeedback


class GoodsFeedbackForm(forms.ModelForm):

    class Meta:
        model = GoodsFeedback
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={'rows': '2'})
        }
