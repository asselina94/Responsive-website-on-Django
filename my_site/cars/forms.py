from django import forms 
from .models import Review
from django.forms import ModelForm
#class ReviewForm(forms.Form):
#    first_name = forms.CharField(label='First name',max_length=100)
#    last_name = forms.CharField(label='Last name',max_length=100)
 #   email = forms.EmailField(label='Email')
  #  review = forms.CharField(label='Please write your review here', 
   #                         widget=forms.Textarea(attrs={'class':'myform',
    #                        'rows':'2','cols':'2'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__" # pass in all model fields as form fileds

        labels = {

            'first_name':"Your First Name",
            'last_name':'Last Name',
            'stars':'Rating'
        }

        error_messages= {

            'stars':{
                'min_value':"YO! Min value is 1",
                'max_value':"YO! YO! Max value is 5"
            }
        }