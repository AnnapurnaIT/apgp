from django import forms
from . import models


#forms starts here
class PostForm(forms.Form):
    def __init__(self,*args, **kwargs):
        self.FormName='नया पद थप्नुहोस'
        super(PostForm, self).__init__(*args, **kwargs)
    post=forms.CharField(
        max_length=100,
        label='पद',
        help_text='पद उल्लेख गर्नुहोस',
        error_messages={'required': 'post cannot be empty'},
         widget=forms.TextInput(attrs={'placeholder': 'सूचना प्रविधि अधिकृत'})
        )
class EmpForm(forms.Form):
    def __init__(self,*args,**kwargs):
        self.FormName='कर्मचारि थप्नुहोस'
        super(EmpForm, self).__init__(*args, **kwargs)
    first_name=forms.CharField(
        max_length=100,
        label='पहिलो नाम',
        help_text='आफ्नो नाम',
        error_messages={
            'required':'पहिलो नाम अनिबार्य छ।'
        },
        widget=forms.TextInput(
            attrs={
                'placeholder':'पहिलो नाम'
            }
        ),
    )
    last_name=forms.CharField(
        max_length=100,
        label='थर',
        help_text='आफ्नो थर',
        error_messages={
            'required':'थर अनिबार्य छ।'
        },
        widget=forms.TextInput(
            attrs={
                'placeholder':'थर'
            }
        ),

    )
    phone_number=forms.CharField(
        max_length=15,
        label='सम्पर्क नं',
        help_text='सम्पर्क नं उल्लेख गर्नुहोस',
        widget=forms.TextInput(
            attrs={
                'placeholder':'XXXXXXXXXXXXXX'
            }
        ),

    )
    email=forms.EmailField(
        label='Enter Your Email',
    )
    emp_post=forms.ModelChoiceField(
        queryset=models.Post.objects.all(),
        required=False,
        empty_label='पद',
        label='कर्मचारि पद',
        help_text='पद छनौट गर्नुहोस',

    )
    section=forms.ModelChoiceField(
        queryset=models.Section.objects.all(),
        required=False,
        empty_label='शाखा',
        label='सम्वन्धित शाखा',
        help_text='शाखा छनौट गर्नुहोस',
        
    )
    emp_weight=forms.ChoiceField(
        choices=models.Choices.IntegerChoices100(),
        required=True,
        label='प्राथमिकता नं',
        help_text='कम अङ्क उच्च प्राथमिकता',
        
    )
    emp_status=forms.ChoiceField(
        choices=models.Choices.StatusChoices(),
        required=True,
        label='कार्यरत अवस्था',
        help_text='कार्यरत अवस्था : पुर्व वा वर्तमान उल्लेख गर्नुहोस'
    )


class SectionForm(forms.ModelForm):
    class Meta:
        model= models.Section
        fields=['sec_name','sec_head']
        labels={
            'sec_name':"शाखा को नाम",
            'sec_head':"शाखाप्रमुख छनौट गर्नुहोस",
        }
        widgets= {
            'sec_name':forms.TextInput(attrs={
                'placeholder':'शाखाको नाम उल्लेख गर्नुहोस',
            }),
            'sec_head': forms.Select(attrs={
                'placeholder':'शाखाप्रमुख छनौट गर्नुहोस'
            })
        }
        

        def clean(self):
            cleaned_data=super().clean()
            sec_head=cleaned_data.get('sec_head')
            if sec_head and sec_head.section != self.instance:
                self.add_error('sec_head','शाखाप्रमुख सम्बन्धित शाखामानै कार्यरत हुनुपर्नेछ')

            return cleaned_data
    
# class ServiceForm


