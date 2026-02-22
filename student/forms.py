from django import forms

from .models import Student
class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"enter a name", "class":"form-control"} ))

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'student_id': forms.NumberInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
        }