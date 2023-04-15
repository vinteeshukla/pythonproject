from django import forms
from .models import DetailForm

# class RatingForm(forms.ModelForm):

#    class Meta:
#       model = Rating
#       fields = ('subject', 'name','rating')



class Detailstored(forms.ModelForm):

   class Meta:
      model = DetailForm
      fields = ('description', 'name','title','mobile','email','password','detail_id')      