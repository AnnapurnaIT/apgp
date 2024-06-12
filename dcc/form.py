from django import forms
# from . import models


#forms starts here
class PostForm(forms.Form):
    post=forms.CharField(
        max_length=100,
        label='पद',
        help_text='पद उल्लेख गर्नुहोस',
        error_messages={'required': 'post cannot be empty'},
         widget=forms.TextInput(attrs={'placeholder': 'सूचना प्रविधि अधिकृत'})
        )

