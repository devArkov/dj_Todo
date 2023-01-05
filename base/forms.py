from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'row': 5
            }),
            'complete': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

    description = forms.CharField(label='Description', required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    complete = forms.BooleanField(label='Complete', initial=False)
