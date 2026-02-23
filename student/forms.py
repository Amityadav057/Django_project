from django import forms

from .models import Student
from .models import Grade
from .models import Subject

class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter a name", "class":"form-control"} ))

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'student_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }   
        
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }        