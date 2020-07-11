from django import forms
from django.core.exceptions import ValidationError

class flist(forms.Form):
    hall = forms.IntegerField(label='ENTER YOUR HALL TICKET NUMBER = ',required = False)

def c_hall(n):
      if len(str(n)) != 3:
             raise ValidationError('enter valid hall ticket number')
            

class valid(forms.Form):
      hall = forms.IntegerField(label='ENTER YOUR HALL TICKET NUMBER = ',required = False,validators=[c_hall])

