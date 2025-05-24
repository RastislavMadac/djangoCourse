from django import forms 

class JokeForm(forms.Form): 

    user_name = forms.CharField( label='Vaše jméno',required=True, max_length=10, error_messages={ 

        'required': 'Jméno nesmí být prázdné', 

        'max_length': 'Prosím vložte kratší jméno', 

    },
     widget=forms.TextInput(attrs={'placeholder': 'Jméno'}) 
    )  

    joke_text = forms.CharField(label='Váš vtip',    widget=forms.Textarea(attrs={'placeholder': 'Sem napište svůj vtip'}),max_length=250) 

    rating = forms.IntegerField(label='Váš rating', min_value=1, max_value=5, widget=forms.TextInput(attrs={'placeholder': '1 - 5'}) ) 