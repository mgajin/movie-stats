from django import forms


class SearchMovie(forms.Form):
    title = forms.CharField(label='Search movie', max_length=30)
