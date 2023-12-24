from django import forms
from .models import Student


class StudentCreateForm(forms.Form):
    name = forms.CharField(max_length=35)
    subject = forms.CharField(max_length= 45)
    un_id = forms.IntegerField()
    verify_date = forms.DateField() 




class StudentUpdateForm(forms.ModelForm):
    class Meta:

        model = Student
        fields = '__all__'




    