from django import forms

from musicapp.models import Artiste
# To house all our forms logics in one file


class AlbumForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Artiste
        fields = (
            'first_name', 'last_name', 'age',
            'song'
        )
