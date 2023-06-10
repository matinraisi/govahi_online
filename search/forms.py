from django import forms

class SearchForm(forms.Form):
    national_id = forms.CharField(max_length=10, label="شماره ملی")