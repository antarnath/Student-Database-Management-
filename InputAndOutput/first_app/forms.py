from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll',
            'class_name' : 'Class Name',
            'address' : 'Student Address',
        }       
        help_texts = {
            'name' : 'Write your full name'
        }
        error_massages = {
            'name' : {'required': 'Your name is required'}
        }