from django import forms


class SearchMovie(forms.Form):
    title = forms.CharField(label='Search movie', max_length=30)


class YearFilter(forms.Form):
    year = forms.CharField(label='Enter year', min_length=4, max_length=4)
