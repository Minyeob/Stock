from django import forms

class SearchForm(forms.Form):
    name = forms.CharField(label='')

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'exampleInputEmail2',
            'placeholder': '검색종목'})


