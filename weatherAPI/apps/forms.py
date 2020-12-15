from django import forms
from .models import History

class HistoryModelForm(forms.ModelForm):

    class Meta:
        
        model = History
        fields = ('city',)



