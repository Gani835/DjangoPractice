from django import forms

class Email(forms.Form):
    Email=forms.EmailField()
    
    def __str__(self):
        return self.Email