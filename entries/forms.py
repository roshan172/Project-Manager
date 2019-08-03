from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('title','author','text',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class': 'textarea', 'placeholder': "Short Title of today's work"})
        self.fields['author'].widget.attrs.update({'class': 'textarea', 'placeholder': " "})
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': "Describe Today's Work"})
