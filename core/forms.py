from django import forms


class LeadGeneratorForm(forms.Form):
    keywords = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Restaurant'}))
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Boston'}))
    leads_num = forms.IntegerField(min_value=1, max_value=1000)

    def __init__(self, *args, **kwargs):
        super(LeadGeneratorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'mb-3'