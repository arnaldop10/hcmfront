from django import forms


class WorkdayForm(forms.Form):
    code = forms.CharField(label='Codigo', max_length=2)
    name = forms.CharField(label='Nombre')
