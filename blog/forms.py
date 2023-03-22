from django import forms 
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        #exclude shows all the fields except that u put in the list
        exclude = ['post']
        # to override the name that django do by default
        # django by default take the name fields like : user_name and make -> User name
        labels = {
            'user_name' : 'Your Name',
            'user_email' : 'Your Email',
            'text' : 'Your Comment',
        }