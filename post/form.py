from django import forms



class Mail(forms.Form):
    ad = forms.CharField(required=True)
    mail = forms.EmailField(required=False)
    text = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['text'].widget.attrs = {'rows': '5', 'cols':'39', 'placeholder': 'Müraciətiniz'}
        self.fields['ad'].widget.attrs = { 'placeholder': 'E-poçt'}